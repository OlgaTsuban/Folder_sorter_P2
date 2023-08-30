# Folder Sorter
<p>Here is the second part of the project "Sorter"</p>
<h2>What is new in the second part of this project? </h2>
<p>In this homework assignment, we will turn the folder cleanup script into a Python package and a command-line script that can be invoked anywhere in the system using the command <b>clean-folder</b>. </p>
<h1>What this project can do ?</h1>
<p>Many people have a folder on their desktop named something like "Sort". Typically, this folder remains unsorted indefinitely.I wrote a script that will sort this folder</p>
<p>This program can sort such extension</p>
<ol>
  <li>Images ('JPEG', 'PNG', 'JPG', 'SVG')</li>
  <li>Video files ('AVI', 'MP4', 'MOV', 'MKV')</li>
  <li>Documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')</li>
  <li>Music ('MP3', 'OGG', 'WAV', 'AMR')</li>
  <li>Archives ('ZIP', 'GZ', 'TAR')</li>
  <li>Unknown extensions</li>
</ol>
<p>The output of the script includes:</p>
<ol>
  <li>A list of files in each category (music, video, photos, etc.)</li>
  <li>A list of all recognized script extensions found in the target folder.</li>
  <li>A list of all extensions that are unknown to the script.</li>
</ol>
<h1>How to use?</h1>
<p>The package is installed in the system using the command <b>pip install -e .</b> (or <b>python setup.py install</b>, requiring administrator privileges). </p>
<p>After installation, the package clean_folder becomes available in the system. </p>
<p>Once the package is installed, the script can be called from anywhere in the system using the command <b>clean-folder</b>.</p>
<p>The command-line script handles command-line arguments in the same way as the Python script.</p>
