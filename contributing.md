# Contributing to Ignition Best Practices

Thank you for your interest in contributing to the Ignition Best Practices repository! This guide explains how to share your knowledge and experience while maintaining a collaborative environment.

## Core Principles

1. There are often multiple valid approaches to solving problems in Ignition
2. Context matters - different solutions may work better in different situations
3. Focus on sharing knowledge, not arguing about "right" vs "wrong"
4. Provide clear examples and explanations

## How to Add Alternative Approaches

When adding alternative approaches to any section:

1. Place them under the "Alternative Approaches" section at the top of the relevant document
2. Follow this format:

```markdown
## Alternative Approaches

### [Practice Name] (e.g., Naming Conventions)

**Approach: [name]**
- Used by: [typical users/systems]
- Benefits: [key advantages]
- Example: [clear example]
- Considerations: [important factors to consider]
```

3. Include at least two common approaches for any new practice
4. Focus on explaining when/why each approach might be useful
5. Avoid claiming any approach is "better" or "correct"

## Example

```markdown
### Tag Naming Conventions

**Approach: snake_case**
- Used by: SQL and Python developers
- Benefits: Matches database naming conventions, improves readability
- Example: `tank_level_high`, `motor_speed_setpoint`
- Considerations: May need conversion for systems expecting camelCase

**Approach: PascalCase**
- Used by: .NET and Java developers
- Benefits: Matches Ignition's internal naming conventions
- Example: `TankLevelHigh`, `MotorSpeedSetpoint`
- Considerations: Database integration may require name transformation
```

## How to Contribute

1. Fork the repository
2. Create a feature branch
3. Add your changes following the format above
4. Submit a pull request with a clear description of your additions

## Pull Request Guidelines

- Keep changes focused and atomic
- Ensure your examples are clear and well-formatted
- Test any code or scripts you include
- Update relevant documentation

## Legal Notice
By contributing to this repository, you agree that your contributions will be licensed under its MIT license. You also acknowledge that any practices or code you contribute are provided without warranty of any kind, and neither you nor the repository maintainers shall be liable for any claims or damages arising from their use.

## Questions or Suggestions?

- Open an issue for discussion
- Propose changes through pull requests
- Respect other contributors' viewpoints

Thank you for helping make Ignition development better for everyone!