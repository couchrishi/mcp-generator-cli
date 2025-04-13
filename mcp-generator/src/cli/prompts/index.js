/**
 * Interactive Prompts Module
 * Handles user interaction through command-line prompts
 */

const inquirer = require('inquirer');
const path = require('path');
const fs = require('fs-extra');
const { logger } = require('../../utils/logger');

/**
 * Run interactive prompts to collect user input
 * @param {Object} options - Command line options
 * @returns {Promise<Object>} User input object
 */
async function runInteractivePrompts(options) {
  const userInput = {
    projectPath: options.project,
    descriptionPath: options.description,
    outputPath: options.output,
    projectType: options.project ? 'existing' : null
  };

  const questions = [];

  // Project type selection if not specified
  if (!userInput.projectType) {
    questions.push({
      type: 'list',
      name: 'projectType',
      message: 'Select project type:',
      choices: [
        { name: 'Existing project', value: 'existing' },
        { name: 'New project', value: 'new' }
      ]
    });
  }

  // Project path if not specified
  if (!userInput.projectPath) {
    questions.push({
      type: 'input',
      name: 'projectPath',
      message: (answers) => {
        const projectType = answers.projectType || userInput.projectType;
        return projectType === 'existing' 
          ? 'Enter path to existing project:' 
          : 'Enter path for new project:';
      },
      default: process.cwd(),
      validate: (input, answers) => {
        const projectType = answers.projectType || userInput.projectType;
        if (projectType === 'existing') {
          return fs.existsSync(input) 
            ? true 
            : 'Project path does not exist. Please enter a valid path.';
        }
        return true;
      }
    });
  }

  // Project description input method
  if (!userInput.descriptionPath) {
    questions.push({
      type: 'list',
      name: 'descriptionInputMethod',
      message: 'How would you like to provide the project description?',
      choices: [
        { name: 'Enter description directly', value: 'direct' },
        { name: 'Provide a file path', value: 'file' }
      ]
    });

    // Direct description input
    questions.push({
      type: 'editor',
      name: 'directDescription',
      message: 'Enter project description:',
      when: (answers) => answers.descriptionInputMethod === 'direct',
      validate: (input) => {
        return input.trim().length > 0 
          ? true 
          : 'Description cannot be empty. Please provide a description.';
      }
    });

    // Description file path
    questions.push({
      type: 'input',
      name: 'descriptionPath',
      message: 'Enter path to description file:',
      when: (answers) => answers.descriptionInputMethod === 'file',
      validate: (input) => {
        return fs.existsSync(input) 
          ? true 
          : 'File does not exist. Please enter a valid path.';
      }
    });
  }

  // Output path if not specified
  if (!userInput.outputPath) {
    questions.push({
      type: 'input',
      name: 'outputPath',
      message: 'Enter output directory for generated files:',
      default: (answers) => {
        const projectPath = answers.projectPath || userInput.projectPath;
        return path.join(projectPath, 'mcp-server');
      },
      validate: (input) => {
        // Output path can be a new directory
        return input.trim().length > 0 
          ? true 
          : 'Output path cannot be empty. Please provide a valid path.';
      }
    });
  }

  // Skip prompts if all required options are provided
  if (questions.length === 0) {
    logger.info('Using provided command line options...');
    return userInput;
  }

  // Run the prompts
  logger.info('Please provide the following information:');
  const answers = await inquirer.prompt(questions);

  // Merge command line options with prompt answers
  return {
    projectPath: userInput.projectPath || answers.projectPath,
    descriptionPath: userInput.descriptionPath || answers.descriptionPath,
    directDescription: answers.directDescription,
    outputPath: userInput.outputPath || answers.outputPath,
    projectType: userInput.projectType || answers.projectType,
    descriptionInputMethod: answers.descriptionInputMethod
  };
}

module.exports = { runInteractivePrompts };