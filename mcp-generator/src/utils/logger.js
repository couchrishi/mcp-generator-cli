/**
 * Logger Utility
 * Provides centralized logging functionality with different log levels
 */

const chalk = require('chalk');

/**
 * Logger class for handling application logs
 */
class Logger {
  constructor() {
    this.verbose = false;
  }

  /**
   * Set verbose mode
   * @param {boolean} isVerbose - Whether to enable verbose logging
   */
  setVerbose(isVerbose) {
    this.verbose = isVerbose;
    this.debug('Verbose logging enabled');
  }

  /**
   * Log an error message
   * @param {string} message - Error message
   * @param {Error} [error] - Optional error object
   */
  error(message, error) {
    console.error(chalk.red('ERROR:'), message);
    if (error && this.verbose) {
      console.error(chalk.red(error.stack || error.message || error));
    }
  }

  /**
   * Log a warning message
   * @param {string} message - Warning message
   */
  warn(message) {
    console.warn(chalk.yellow('WARNING:'), message);
  }

  /**
   * Log an info message
   * @param {string} message - Info message
   */
  info(message) {
    console.info(chalk.blue('INFO:'), message);
  }

  /**
   * Log a success message
   * @param {string} message - Success message
   */
  success(message) {
    console.info(chalk.green('SUCCESS:'), message);
  }

  /**
   * Log a debug message (only in verbose mode)
   * @param {string} message - Debug message
   */
  debug(message) {
    if (this.verbose) {
      console.debug(chalk.gray('DEBUG:'), message);
    }
  }

  /**
   * Log a plain message without any prefix
   * @param {string} message - Message to log
   */
  log(message) {
    console.log(message);
  }
}

// Create a singleton instance
const logger = new Logger();

module.exports = { logger };