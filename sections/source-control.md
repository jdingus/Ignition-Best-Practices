# Source Control Best Practices

## Overview
Using source control systems like Git for Ignition projects enables collaboration, version tracking, and safe deployments. Adopting best practices ensures efficient management of changes.

---

## Tips and Recommendations

- **Organize Projects in Source Control**
  - Store each Ignition project in its own repository for clarity and isolation.
  - Use a descriptive repository name, such as `production-monitoring-system`.

- **Branch Management**
  - Use three main branches:
    - `main` (or `master`): Stable, production-ready code.
    - `testing`: For quality assurance and testing changes.
    - `development`: Active development work.
  - Create feature branches for new work and merge them back to `development` once completed.

- **Track Ignition Resources**
  - Include:
    - Gateway backups (.gwbk).
    - Tags exported as JSON.
    - Project files (e.g., Perspective Views, Vision Windows).
    - Scripts and libraries.
  - Avoid committing dynamically generated or temporary files like `.resources`.

- **Automate Commits**
  - Use Gateway Event scripts to automatically commit changes when saving in the Ignition Designer.

- **Commit Regularly**
  - Make small, atomic commits with descriptive messages.
  - Example: `git commit -m "Added new chart to production dashboard"`.

---

## Collaboration Tips

- **Pull Requests**
  - Use pull requests to review code before merging into `testing` or `main` branches.
  - Assign reviewers and include testing notes.

- **Conflict Resolution**
  - Communicate with team members to resolve merge conflicts promptly.
  - Test resolved changes thoroughly.

- **Documentation**
  - Include clear README files and comments within scripts to describe functionality.

---

## Tools and Techniques

- **Git Hooks**
  - Use pre-commit hooks to enforce coding standards and validate JSON/tag files.

- **Continuous Integration/Continuous Deployment (CI/CD)**
  - Set up pipelines to automatically test, build, and deploy projects.
  - Example: Run automated tests on feature branches before merging.

- **Backup Strategy**
  - Regularly back up repositories to an external location.
  - Include database and Gateway backups for complete recovery.

---

## Links to More Information
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [Version Control in Ignition](https://docs.inductiveautomation.com/display/DOC81/Version+Control+and+Collaboration)

---

Feel free to contribute additional tips or corrections by submitting a pull request!
