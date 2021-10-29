# Mac related Runbooks

## Using CLI to find software updates

```console
$ softwareupdate -l
Software Update Tool

Finding available software
Software Update found the following new or updated software:
* Label: Command Line Tools for Xcode-13.0
  Title: Command Line Tools for Xcode, Version: 13.0, Size: 528803K, Recommended: YES,
* Label: Safari15.0BigSurAuto-15.0
  Title: Safari, Version: 15.0, Size: 119059K, Recommended: YES,
```

## Using CLI to do software updates

```console
$ softwareupdate -i "Command Line Tools for Xcode-13.0"  # Has to match the label exactly 
Software Update Tool

Finding available software

Downloaded Command Line Tools for Xcode
Installing Command Line Tools for Xcode
Done with Command Line Tools for Xcode
Done.
```

## Using CLI to save password to keychain and retrieve them

- Add a new password for account (`-a`) on service (`-s`) with label (`-l`)

    ```console
    $ security add-internet-password -a sandip@example.com -s github.com -l "personal access token"  -w
    password data for new item:
    retype password for new item:
    ```

- Retrieve the password.

    ```console
    $ security find-internet-password -a sandip@example.com -s github.com -l "personal access token"  -w
    test
    ```

- You cannot overwrite an existing password unless you provide the `-U` parameter.

    ```console
    $ security add-internet-password -a sandip@example.com -s github.com -l "personal access token"  -w
    password data for new item:
    retype password for new item:
    security: SecKeychainAddInternetPassword <NULL>: The specified item already exists in the keychain.

    $ security add-internet-password -U -a sandip@example.com -s github.com -l "personal access token"  -w
    password data for new item:
    retype password for new item:
    $
    ```

- If you want non-interactive input, provide the password after the `-w` parameter (`-w` always has to be the last
  parameter for this tool). Obviously, this is very insecure!

    ```console
    $ security add-internet-password -U -a sandip@example.com -s github.com -l "personal access token"  -w 'some password'
    $ security find-internet-password -a sandip@example.com -s github.com -l "personal access token"  -w
    some password
    ```
