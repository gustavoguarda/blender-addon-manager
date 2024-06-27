# Blender Addon Manager

This script allows you to backup and restore enabled addons in Blender. It is designed to be run from the command line and can be used in headless mode (without the Blender UI).

## Features

- **Backup Addons**: Save the list of enabled addons to a file.
- **Restore Addons**: Enable addons from a previously saved file.

## Prerequisites

- Blender 4.1.1 or later
- Python 3.x

## Installation

1. Download and install Blender from the [official website](https://www.blender.org/download/).
2. Ensure Blender's executable is in your system's PATH or note its location.

## Usage

1. Clone this repository or download the script `addon_manager.py`.

```sh
git clone https://github.com/gustavoguarda/blender-addon-manager.git
cd blender-addon-manager
```

2. Run the script using Blender's command line interface.

#### Backup Addons
```sh
/path/to/blender --background --python /path/to/addon_manager.py -- backup
```

#### Restore Addons
```sh
/path/to/blender --background --python /path/to/addon_manager.py -- restore
```

## Example

Assuming Blender is installed in /opt/blender-4.1.1-linux-x64 and the script is located in ~/blender/addon_manager.py:

#### Backup Addons
```sh
/opt/blender-4.1.1-linux-x64/blender --background --python ~/blender/addon_manager.py -- backup
```

#### Restore Addons
```sh
/opt/blender-4.1.1-linux-x64/blender --background --python ~/blender/addon_manager.py -- restore
```