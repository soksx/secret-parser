# Secret Parser Action

Replaces GitHub Actions secrets referenced in files with their raw values.

## Inputs

### `filename`

**Required** File where GitHub Actions Secrets references should be parsed and replaced.

### `secret-name`

**Required** Name of secret to search for in the designated file.

### `secret-value`

**Required** Value of secret to replace reference with in designated file.

## Example usage

1. Create a file in the repository which references GitHub actions secret. For example, `test.json`:

```
{
  "config_key_1" : "${{ secrets.replace_name1 }}",
  "config_key_2" : "${{ secrets.replace_name2 }}",
  "config_key_3" : "${{ secrets.replace_name3 }}",
}
```

2. Create a GitHub action secret with a key of: `important_value1,important_value2,important_value3`

3. Add the following to your workflow configuration file (parameters shown below are for this demonstration only):

```
uses: soksx/secret-parser@v2
with:
  filename: test.json
  secrets-dictionary: |
    replace_name1:${{ secrets.important_value1 }}
    replace_name2:${{ secrets.important_value2 }}
    replace_name3:${{ secrets.important_value3 }}
```

4. During workflow execution, `test.json` (or a file of one's choosing) will be parsed and the reference to a GitHub secret will be replaced with the corresponding secret value.