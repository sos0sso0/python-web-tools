# Technical Notes

## PyScript JavaScript Interop

### Current Implementation

The current implementation in `web/data_processing.py` uses a custom pattern to expose Python functions to JavaScript:

```python
# Manual JavaScript object creation
if not hasattr(js, 'pyscript'):
    js.pyscript = js.Object.new()
# ... etc

# Custom function lookup
def get_exposed_function(name):
    if name in _exposed_functions:
        return _exposed_functions[name]
    else:
        raise ValueError(f"Function '{name}' is not exposed to JavaScript")

js.pyscript.interpreter.globals.get = get_exposed_function
```

### Why This Pattern?

This pattern was inherited from the original embedded code in `index.html`. It works with the current JavaScript code that expects:
```javascript
const pythonFunc = pyscript.interpreter.globals.get('process_excel_merge');
pythonFunc(excelMergeFiles);
```

### Future Improvement Considerations

PyScript's official documentation recommends using:
- `pyscript.write()` for output
- `@when()` decorator for event handling
- Direct function exposure patterns

However, changing this would require:
1. Updating JavaScript code in `index.html`
2. Testing all functionality thoroughly
3. Ensuring compatibility with PyScript 2024.1.1

### Decision

**For this PR:** Keep the existing working pattern to minimize risk and maintain compatibility.

**For future:** Consider refactoring to use PyScript's official APIs when doing a larger update to the web interface.

### References

- PyScript Documentation: https://docs.pyscript.net/
- Current PyScript version: 2024.1.1
- Pattern source: Original `index.html` embedded code

## Code Review Notes

The automated code review flagged this pattern as potentially fragile. This is a valid concern for future development, but not a blocker for this PR since:

1. This code was already working in production (embedded in index.html)
2. The extraction didn't modify the logic, only moved it
3. Changing the pattern would require extensive testing
4. The user's primary need is understanding how to update the interface, which the documentation now addresses

## Recommendation

Monitor PyScript releases for:
- Breaking changes to JavaScript interop
- New recommended patterns
- Migration guides

When PyScript releases a new major version or the interop pattern shows issues, revisit this implementation.
