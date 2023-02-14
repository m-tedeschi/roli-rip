<p align="center">roli-rip<br>Scrapes the current Premium owners of Roblox items from the Rolimon's website<hr></p>
<p align="left"><b>Requirements:</b><br><ul><li><a href="https://www.google.com/chrome/">Google Chrome</a></li><li><a href="https://www.python.org/downloads/">Python</a> (recommended version: 3.10 or newer)</li><li><a href="https://pypi.org/project/selenium/">Selenium for Python</a> (from command line: <code>pip install selenium)</code></li><li><a href="https://chromedriver.chromium.org/downloads">ChromeDriver: WebDriver for Chrome</a></li></ul></p>
<br>
<b>Usage:</b><br>
<ol><li>Ensure all dependencies are installed and properly configured</li><li>Run <code>roli-rip.py</code> with Python. From command line: <code>python roli-rip.py</code></li><li>Enter an output file name. Make sure to include the extension. I recommend `.txt`</li><li>Navigate to the Rolimon's page for the item you wish to scrape. The item ID is the number at the end of the URL, as shown below:</li><li>Copy and paste the ID into the program, hit enter to begin the script</li><li>The script should run autonomously in the background. Depending on how many owners the item has, this could take a while. Feel free to make a coffee or something while you wait</li><li>If all went well, you should find your output file in the same directory that the script ran in with all of the owners' names, from newest to oldest owner</li></ol>
<br>
<b>Known Issues / To-Do List:</b>
<ul><li>I whipped this together in a half-hour, there's literally no error checking for the following:<ul><li>Bad file names</li><li>Page loading times / network drops (if your internet takes > 1 sec to load the page, tough luck)</li></ul><li>Doesn't check for existing output file -- although it <i>does</i> append instead of completely overwrite</li><li>If an error states something about 'WebDriver' missing, you probably need to add the path to ChromeDriver to your System Environment Variables ("Path" variable)</li><li><b>TO-DO:</b> make process start minimized / in the background</li><b>TO-DO:</b> add feature to check if user also owns other items</li></ul></p>
