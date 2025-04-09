/**
 * Configuration Utility
 * Manages application configuration and settings
 */

const path = require('path');
const fs = require('fs-extra');
const dotenv = require('dotenv');
const { logger } = require('./logger');

// Load environment variables from .env file
dotenv.config();

/**
 * Configuration class for managing application settings
 */
class Config {
  constructor() {
    this.config = {
      // Default configuration values
      llm: {
        provider: process.env.LLM_PROVIDER || 'gemini',
        apiKey: process.env.LLM_API_KEY || '',
        maxTokens: parseInt(process.env.LLM_MAX_TOKENS || '4096', 10),
        temperature: parseFloat(process.env.LLM_TEMPERATURE || '0.7'),
        timeout: parseInt(process.env.LLM_TIMEOUT || '30000', 10)
      },
      paths: {
        templates: path.resolve(__dirname, '../../templates'),
        data: path.resolve(__dirname, '../../data')
      },
      registry: {
        serversFile: path.resolve(__dirname, '../../data/registry/servers.json'),
        toolsFile: path.resolve(__dirname, '../../data/registry/tools.json')
      }
    };

    // Create required directories if they don't exist
    this.ensureDirectories();
  }

  /**
   * Get configuration value
   * @param {string} key - Configuration key (dot notation supported)
   * @param {*} defaultValue - Default value if key not found
   * @returns {*} Configuration value
   */
  get(key, defaultValue = null) {
    const keys = key.split('.');
    let value = this.config;

    for (const k of keys) {
      if (value === undefined || value === null || !Object.prototype.hasOwnProperty.call(value, k)) {
        return defaultValue;
      }
      value = value[k];
    }

    return value;
  }

  /**
   * Set configuration value
   * @param {string} key - Configuration key (dot notation supported)
   * @param {*} value - Configuration value
   */
  set(key, value) {
    const keys = key.split('.');
    let current = this.config;

    for (let i = 0; i < keys.length - 1; i++) {
      const k = keys[i];
      if (!Object.prototype.hasOwnProperty.call(current, k)) {
        current[k] = {};
      }
      current = current[k];
    }

    current[keys[keys.length - 1]] = value;
  }

  /**
   * Ensure required directories exist
   */
  ensureDirectories() {
    try {
      // Ensure templates directory exists
      fs.ensureDirSync(this.get('paths.templates'));
      fs.ensureDirSync(path.join(this.get('paths.templates'), 'server'));
      fs.ensureDirSync(path.join(this.get('paths.templates'), 'tools'));
      fs.ensureDirSync(path.join(this.get('paths.templates'), 'providers'));

      // Ensure data directory exists
      fs.ensureDirSync(this.get('paths.data'));
      fs.ensureDirSync(path.join(this.get('paths.data'), 'registry'));

      // Create empty registry files if they don't exist
      const serversFile = this.get('registry.serversFile');
      if (!fs.existsSync(serversFile)) {
        fs.writeJsonSync(serversFile, { servers: [] }, { spaces: 2 });
      }

      const toolsFile = this.get('registry.toolsFile');
      if (!fs.existsSync(toolsFile)) {
        fs.writeJsonSync(toolsFile, { tools: [] }, { spaces: 2 });
      }
    } catch (error) {
      logger.warn(`Failed to create required directories: ${error.message}`);
    }
  }
}

// Create a singleton instance
const config = new Config();

module.exports = { config };