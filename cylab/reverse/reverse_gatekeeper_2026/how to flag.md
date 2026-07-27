## Category: Reverse Engineering

## Topic: Input validation bypass through mixed radix interpretation

## Vulnerability: Type Confusion / Input Validation Bypass

The program validates input as both decimal and hexadecimal, but uses different conversion methods. This allows a 3-character hexadecimal input to represent a value in the valid range (1000-9999) while passing the length check.

## Exploit Analysis

### Program Flow
1. User inputs a numeric code
2. Program validates if input is valid decimal or valid hexadecimal
3. Converts using appropriate method (atoi for decimal, strtol for hex)
4. Checks if value is between 1000-9999
5. **Critical Check**: If value < 10000 AND string length == 3, reveals flag

### The Vulnerability
```c
// Decimal validation - checks if all characters are digits (0-9)
if (is_valid_decimal(input)) {
    value = atoi(input);  // Converts decimal string to int
}
// Hex validation - checks if all characters are hex digits (0-9, a-f, A-F)
else if (is_valid_hex(input)) {
    value = strtol(input, NULL, 16);  // Converts hex string to int
}

// The vulnerability: A 3-character hex string can represent numbers >= 1000
if (value < 10000 && strlen(input) == 3) {
    reveal_flag();
}
```

### Solution
Input a 3-character hexadecimal number that represents a value between 1000-9999:

- Minimum 3-digit hex value >= 1000: `0x3E8 = 1000`
- Input: `3E8`

### Verification
```
Enter a numeric code (must be > 999 ): 3E8
Access granted: }3f31ac64_999_TG_xeh_tigid_3{FTCocip
```

### Flag Decoding
The flag is printed in reverse with "ftc_oc_ip" inserted every 4 characters:

**Raw Output:** `}3f3ftc_oc_ip1ac6ftc_oc_ip4_99ftc_oc_ip9_TGftc_oc_ip_xehftc_oc_ip_tigftc_oc_ipid_3ftc_oc_ip{FTCftc_oc_ipocipftc_oc_ip`

**Cleaned (remove "ftc_oc_ip"):** `}3f31ac64_999_TG_xeh_tigid_3{FTCocip`

**Reversed:** `picoCTF{3di_git_hex_GT9_99_4_6ca1_3f3}`

## Python Solution

```python
# Clean and reverse the flag
def decode_flag(raw_output):
    # Remove the inserted "ftc_oc_ip" strings
    cleaned = raw_output.replace("ftc_oc_ip", "")
    # Reverse the string
    flag = cleaned[::-1]
    return flag

# Example usage
raw = "}3f3ftc_oc_ip1ac6ftc_oc_ip4_99ftc_oc_ip9_TGftc_oc_ip_xehftc_oc_ip_tigftc_oc_ipid_3ftc_oc_ip{FTCftc_oc_ipocipftc_oc_ip"
flag = decode_flag(raw)
print(f"Flag: {flag}")
# Output: picoCTF{3di_git_hex_GT9_99_4_6ca1_3f3}
```

## Step-by-Step Exploitation

### Step 1: Identify the Vulnerability
- The program accepts both decimal and hexadecimal inputs
- `is_valid_decimal()` checks for digits 0-9
- `is_valid_hex()` checks for hex characters 0-9, a-f, A-F
- A 3-character hex string can represent values up to 4095 (0xFFF)

### Step 2: Find Valid Input
- Need a 3-character hex value >= 1000
- Possible values: 0x3E8 (1000) through 0xFFF (4095)
- Any hex string in this range works

### Step 3: Exploit
```bash
$ nc green-hill.picoctf.net 55952
Enter a numeric code (must be > 999 ): 3E8
Access granted: }3f31ac64_999_TG_xeh_tigid_3{FTCocip
```

### Step 4: Decode the Flag
```python
# Method 1: One-liner
flag = raw_output.replace("ftc_oc_ip", "")[::-1]

# Method 2: Step by step
cleaned = raw_output.replace("ftc_oc_ip", "")
flag = cleaned[::-1]
```

## Prevention / Mitigation
- Use consistent input validation and conversion methods
- Don't accept multiple number formats unless properly sanitized
- Validate length and value range together before conversion
- Use secure coding practices for input handling

## Flag
```
picoCTF{3di_git_hex_GT9_99_4_6ca1_3f3}
```