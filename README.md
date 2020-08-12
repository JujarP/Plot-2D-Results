# Plot-2D-Results

Python script reads timestamped results file &amp; plots variables on 2D grid &amp; saves plot variable as timestamped image

# Description

Python script to plot variables on a 2D grid where the data is read from time stamped files.
* Suppose you have a series of time stamped results files: 12.0000.plt, 14.0000.plt, 16.0000.plt, etc
* The script loops through all those files in the working directory and plots variables onto a 2D grid
* Suppose those files have the structure as follows:

| x coordinate | y coordinate | variable 1, e.g. Temp | Variable 2, e.g. Velocity |
|---|---|---|---|
| Some data | Some data | Some data | Some data |
| ... | ... | ... | ... |
| Last data point | Last data point | Last data point | Last data point |

* This script loops through all time stamped results files and plots a figure of a variable against the x and y coordinates creating a colour map
* The figures are time stamped and are also saved as timestamps in their file names
* E.g. 12.0000.png, 14.0000.png, etc
* Ultimately this allows users to stitch the images together and create animations

## Installation

Use a Python environment of your choice. This was created in Anaconda Spyder.

## Usage

The main user inputs are:

* Change the extension of your files that contains your data. E.g. .plt, .dat, .txt, etc

```python
        if filepath.endswith(".plt"):
```

* Change your variable names. In your file you must have headers. In this example headers are x, y, ux, uy etc.

```python
            x = data["x"].values                                        #Assign variable name
            y = data["y"].values                                        #Assign variable name
            xy_ux = data["ux"].values                                   #Assign variable name
            xy_uy = data["uy"].values                                   #Assign variable name
            xy_uz = data["uz"].values                                   #Assign variable name
            xy_dux = data["dux"].values                                 #Assign variable name
            xy_duy = data["duy"].values                                 #Assign variable name
            xy_duz = data["duz"].values                                 #Assign variable name
``` 

* Change the variable you want to plot

```python
            var=xy_uz                                    #Which variable do you want to plot?

```

* There are also some graphing options you can change and these are under the section 

```python
##################################################
################GRAPHING OPTIONS##################
##################################################
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Support

Feel free to contact me jujar dot panesar at gmail dot com
