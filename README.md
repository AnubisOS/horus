
# horus

A Pharaonic fetch tool for Arch Linux written in Python.


## Screenshots

* Pharo
  ![App Screenshot](res/Pharo.png)
* Dark Pharo 
  ![App Screenshot](res/Dark_Pharo.png)
* Nord
  ![App Screenshot](res/Nord.png)
* Nord inverted
  ![App Screenshot](res/Nord_rev.png)


## Installation

### Install : 
* use 
```
  git clone https://github.com/HushmKun/horus.git
  cd horus/
  make install
```
### Update :
* use 
``` 
  git clone https://github.com/HushmKun/horus.git
  cd horus/
  make update
```
### Uninstall :
* use 
``` 
  cd horus/
  make uninstall
```

## Usage/Examples

* Uses default config.  
```Bash
  horus
```

* Uses a custom made config file ( example of config file found [here](res/papyri.cfg) )
```Bash
  horus -c ./path/to/config
```

* Uses a cmdline arguments   
```Bash 
  horus -fg 100 100 100 -bg 25 25 25 
```


## Features

- Pure python (No dependecies).
- Relatively fast.
- CLI arguments.


## Roadmap

- [x] Add config file to maximize customizations.
- [x] Add argparse to allow CLI arguments.
- [ ] currently unknown, If you want to add some features open an Issue or maybe wanna do it yourself with PR.


## Acknowledgements

 - [Haruno](https://github.com/Haruno19) was my literal role model to reach.
 - [dylanaraps](https://github.com/dylanaraps) for making fetch tools in general.
 - [Thijs van Ede](https://github.com/Thijsvanede) for making the StructuredFormatter class.


## License

This Project is Licensed as [MIT](https://choosealicense.com/licenses/mit/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


