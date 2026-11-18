# Home Lab Engineering Projects

## Overview

This directory contains hands-on engineering projects developed as part of the RHEL Engineer Home Lab.

The purpose of these projects is to develop practical Linux administration, troubleshooting, scripting, automation, security, and Site Reliability Engineering (SRE) skills.

Each project should solve a real operational problem within the home lab while providing opportunities to practice and demonstrate technical proficiency.

## Engineering Objectives

- Strengthen RHEL administration and troubleshooting skills.
- Develop proficiency in Bash and Python.
- Apply configuration management and automation principles.
- Practice system monitoring, maintenance, and recovery.
- Build reusable operational tools.
- Establish disciplined engineering and change-management procedures.
- Document technical decisions, testing, and lessons learned.

## Projects

| Project | Description | Status |
|---|---|---|
| RHEL Patching Guide | Interactive application for planning, executing, validating, and documenting RHEL maintenance | In Development |
| RHEL Troubleshooting Guide | Future application using structured troubleshooting methodology and historical incident records | Planned |

## Project Development Standards

Each project should follow these principles:

1. **Understand before automating:** Learn and execute the underlying Linux commands manually before scripting them.
2. **Build incrementally:** Develop small, testable components before adding complexity.
3. **Prioritize safety:** Use read-only operations during initial development and require safeguards before making system changes.
4. **Test before deployment:** Validate new functionality in an isolated test environment when available.
5. **Document changes:** Maintain project documentation and meaningful Git commits.
6. **Verify results:** Confirm that completed operations achieve their intended outcomes.

## Repository Organization

Each project should maintain its own directory, documentation, source code, and tests as appropriate.

Projects remain part of the parent `rhel-engineer-home-lab` Git repository unless there is a clear reason to separate them.

## Long-Term Goal

Develop a portfolio of reliable, documented engineering tools that demonstrate practical Linux administration, Python development, troubleshooting, and automation capabilities.