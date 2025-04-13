/**
 * Error Handling Utility
 * Provides centralized error handling functionality
 */

const { logger } = require('./logger');

/**
 * Custom error classes
 */
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = 'ValidationError';
  }
}

class ProjectError extends Error {
  constructor(message) {
    super(message);
    this.name = 'ProjectError';
  }
}

class LLMError extends Error {
  constructor(message) {
    super(message);
    this.name = 'LLMError';
  }
}

class GenerationError extends Error {
  constructor(message) {
    super(message);
    this.name = 'GenerationError';
  }
}

/**
 * Handle errors in a centralized way
 * @param {Error} error - The error to handle
 */
function handleError(error) {
  if (error instanceof ValidationError) {
    logger.error(`Validation Error: ${error.message}`);
  } else if (error instanceof ProjectError) {
    logger.error(`Project Error: ${error.message}`);
  } else if (error instanceof LLMError) {
    logger.error(`LLM Interaction Error: ${error.message}`);
  } else if (error instanceof GenerationError) {
    logger.error(`Code Generation Error: ${error.message}`);
  } else {
    logger.error(`Unexpected Error: ${error.message}`, error);
  }
}

module.exports = {
  ValidationError,
  ProjectError,
  LLMError,
  GenerationError,
  handleError
};