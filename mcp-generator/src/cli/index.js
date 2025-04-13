/**
 * CLI Interface Component
 * Handles command-line arguments, options, and interactive prompts
 */

const { Command } = require('commander');
const inquirer = require('inquirer');
const chalk = require('chalk');
const path = require('path');
const fs = require('fs-extra');
const { version } = require('../../package.json');
const { runInteractivePrompts } = require('./prompts');
const { logger } = require('../utils/logger');
const { handleError } = require('../utils/errors');

// Create a new Command instance
const program = new Command();

// Configure the CLI program
program
  .name('generate-mcp-server')
  .description('Generate customized MCP servers based on natural language descriptions')
  .version(version)
  .option('-p, --project <path>', 'Path to existing project')
  .option('-d, --description <path>', 'Path to project description file')
  .option('-o, --output <path>', 'Output directory for generated files')
  .option('-v, --verbose', 'Enable verbose logging')
  .option('-h, --help', 'Display help information')
  .action(async (options) => {
    try {
      // Set verbose logging if specified
      if (options.verbose) {
        logger.setVerbose(true);
      }

      logger.info('Starting MCP Server Generator CLI...');
      
      // Get user input through interactive prompts if not provided as options
      const userInput = await runInteractivePrompts(options);
      
      // Process the project (analyze existing or create new)
      await processProject(userInput);
      
      logger.success('MCP Server Generator completed successfully!');
    } catch (error) {
      handleError(error);
      process.exit(1);
    }
  });

/**
 * Process the project based on user input
 * This is a placeholder function that will be implemented in later tasks
 * @param {Object} userInput - User input from CLI options or interactive prompts
 */
async function processProject(userInput) {
  const { projectPath, descriptionPath, directDescription, outputPath, projectType, descriptionInputMethod } = userInput;
  
  logger.info(`Processing ${projectType} project...`);
  logger.info(`Project path: ${projectPath}`);
  logger.info(`Description path: ${descriptionPath || 'Direct input'}`);
  logger.info(`Output path: ${outputPath}`);
  
  // Import required components
  const { analyzeExistingProject, createNewProject } = require('../analyzer');
  const { processProjectDescription } = require('../llm');
  const { selectServersAndTools } = require('../registry');
  const { generateMCPServer, generateDocumentation } = require('../generator');
  
  try {
    // Analyze or create project
    let projectInfo;
    if (projectType === 'existing') {
      logger.info('Analyzing project...');
      projectInfo = await analyzeExistingProject(projectPath);
    } else {
      logger.info('Creating new project...');
      projectInfo = await createNewProject(projectPath);
    }
    
    // Get project description
    const description = descriptionInputMethod === 'direct'
      ? directDescription
      : await fs.readFile(descriptionPath, 'utf8');
    
    // Process description with LLM
    logger.info('Processing project description...');
    const llmOutput = await processProjectDescription(projectInfo, description);
    
    // Select appropriate servers and tools
    logger.info('Selecting appropriate MCP servers and tools...');
    const selection = await selectServersAndTools(llmOutput.requirements);
    
    // Generate MCP server code
    logger.info('Generating MCP server code...');
    const generationResult = await generateMCPServer(selection, projectInfo, llmOutput, outputPath);
    
    // Generate documentation
    await generateDocumentation(selection, outputPath);
  
    // Output presentation
    logger.info('MCP server generated successfully!');
    logger.info(`Generated files are available at: ${outputPath}`);
  } catch (error) {
    handleError(error);
    throw error;
  }
}

module.exports = { program };