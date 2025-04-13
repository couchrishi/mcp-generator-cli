#!/usr/bin/env node

/**
 * MCP Server Generator CLI
 * Main entry point for the CLI application
 */

const { program } = require('../src/cli');

// Execute the CLI program
program.parse(process.argv);

// If no arguments are provided, show help
if (process.argv.length === 2) {
  program.help();
}