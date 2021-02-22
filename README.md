# pyWPB

`pyWPB` - Python Web Page Builder

HTML `Creator` using `Python`

![](https://img.shields.io/badge/pypi-0.1.9-blue)![](https://img.shields.io/badge/python-3.7|3.8|3.9-lightblue)![](https://img.shields.io/badge/Licence-MIT-lightgray)![](https://img.shields.io/badge/status-alpha-orange)![](https://img.shields.io/badge/pipeline-passed-green)![](https://img.shields.io/badge/testing-passing-green)


**key features:**

- Building a Header Page
- Style to Body tag
- Create Tables using dataframe pandas
- Insert images from graph application such seaborn, matplotlib and any other
- Coloring text and styles separately
- Personalised Footer
- Automatically creates texto to Images and Tables
- Embedded videos from your own site or from Youtube
- Create Frames easily
- Ordered and Unordered and description lists in one command line

## Where to use
- Nicely to be used on embedded in Flask applications. You create a dynamic page very easy
- You can also create dynamic pages in your Django applications
- If you have other applications working in a batch mode, you can create many dynamics pages in background
- You don't need to know HTML5, CSS or some stuff like that, you just know Python

<BR><BR>
<hr>

## Install

```shell
pip install pywpb
```
<hr>

## Current Modules

To use any `PYWPB` module you must instantiates all of then using the follow command:

### **Header**

There is only one method to create a page. And you need to run it before anything else.

### **Creator**

Create a new Web Page with a minimal configuration. You must run this step before any other command. You can choose you lang, if ommited, the default lan will be english.

`sintax`:
```python
from pywpb import pywpb as wpb

h = wpb.header(charset='utf-8', 
           page_size=[21.0, 29.7, 2.0],
           margin=[0.25, 115],
           background='transparent',
           title='pywpb Page without Title')
```
The values above are default, but you can change to:

**The charset**
- `ASCII` | `ANSI` | `ISO-8859-1` | `UTF-8`

**Page Size**
- `Right`=21.0 | `Left` 29.7 | `Margin` 2.0

**Margin**
- `margin-bottom` | `line-height`

**Background**
- You can change to any wish color 

**Title**
- Title of you page. If you don't give a text, the text above will be provided

`Prints such a string:`

```html
<!DOCTYPE html PUBLIC "-// W3C // DTD XHTML 1.0 Strict // EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title>pywpb Page without Title</title>
	<meta name="generator" content="pywpb - Python Web Page Builder"/>
	<meta name="created" content="2021/02/17T16:44:08"/>
	<meta name="changed" content="00:00:00"/>
	<style type="text/css">
		@page { size: 21.0cm 29.7cm; margin: 2.0cm }
		p { margin-bottom: 0.25cm; line-height: 115%; background: transparent }
	</style>
</head>

```

### **Body**

`sintax`:
```python
from pywpb import pywpb as wpb

b = pwb.body(margin=0, line=100, 
         link='#000080', 
		 vlink='#800000',
         lang='eng')
```

The values above are default, but you can change to:

**Margin**
- Margin of body. Normally zero.

**Line**
- Line will be `100`%

**Links**
- The color of the links on the page. The first is the `link never clicked`. The other is the `visited Link`.

`Prints such a string:`
```html
	<body lang="eng" link="#000080" vlink="#800000" dir="ltr">
		<p style="margin-bottom: 0cm; line-height: 100%"><br/>
		</p>
```
<hr>

### **Body Methods**

The `Body Class` has many methods that you can see below.

<hr>

#### **h (headings)**

The `<h1>` to `<h6>` tags are used to define HTML headings.

`<h1>` defines the most important heading. `<h6>` defines the least important heading.

`sintax`:
```python
from pywpb import pywpb as wpb

b = wpb.body() # keeping default values for body

b.h(text='Headings have no text', 
    size=5, background='white', 
    align='left', 
	color='black', 
	shadow=False)
```

**Text**
- The text that you want to write on the headings

**Size**
- As previously presented, this is the size ranging from one to six

**Background**
- The background `color`. Make your choice!

**Align**
- The align of the headings. Can be:

	`left` | `center` | `right` | `ustify`

**Color**
- The `color` of the text to be write on headings. Make your choice!

**Shadow**
- If you want a elegant text with shadow, just change to `True`

`Prints such a string:`
```html
		<hr style="height:1px; border-width:0; color:gray;background-color:gray">
```

<hr>

#### **Text Color**

If you want a text with different color, use this method to write a new text on the page. This method don't insert line feed.

`Sintax:`
```python
from pywpb import pywpb as wpb

b = wpb.body() # keeping default values for body

b.color_text(text='no text provided',
			 color='black')
```
`Prints such a string:`
```html
<span style="color:black">this is my text</span>
```

#### **Write a Text**

This method writes a text, any one that you provided in text argument.

`Sintax`
```python
from pywpb import pywpb as wpb

b = wpb.body() # keeping default values for body

b.w_text('another text to see line feed',3)
```
There is no limit to text. If you have a big text, the better way is to load text using `wpIO`. See `loading text from file`.

*line_feed* is the number of lines will be jump using tag `<BR>`.

`Prints such a string:`
```html
another text to see line feed<BR><BR><BR>
```
<hr>

`Sintax`
```python
from pywpb import pywpb as wpb

b = wpb.body() # keeping default values for bod

text = b.change_text_color(color='blue', text='testing text one changing color', text_to='one')
```

`Prints such a string:`
```html
testing text <span style="color:blue">one </span> changing color<BR><BR>
```
After you changed the color text, you must write the text using `w_text` method.

<hr>

#### **Bold Text**

Made bold text.

`Sintax`
```python
from pywpb import pywpb as wpb

b = wpb.body() # keeping default values for bod

text = b.bold_text(self, text='no text provided', text_to='text')
```

The word `text` will be bold.

<hr>

#### **Italic Text**

Made Italic text.

`Sintax`
```python
from pywpb import pywpb as wpbb

b = wpb.body() # keeping default values for bod

text = b.italic_text(self, text='no text provided', text_to='text')
```
<hr>

#### **Horizontal Line**

The `<hr>` tag defines a thematic break in an HTML page. 
The `<hr>` element is most often displayed as a horizontal rule that is used to separate content (or define a change) in an HTML page.

`Sintax`
```python
from pywpb import pywpb as wpb

b = wpb.body() # keeping default values for bod

b.hline(height=1, border=0, color='gray', background='gray')
```

#### **Writing Table**

`Sintax`
```python
from pywpb import pywpb as wpb

b = wpb.body() # keeping default values for bod

df = pd.DataFrame({ 'id': [1,2,3], 
					'Elapsed_time': [11,21,31],
					'Total_Value': [3.5, 4.2 , 5.1]})

b.w_table(df,alt_text='My Table without footer',foot=False)
```
**data**
- The `data` is a `Pandas DataFrame`.
- Big dataset with many columns or lines is not a good idea.
- May be use `head()` to is good way.

**border** 
- That's the thickness of the border

**Align**
- The align table

**Collapse**
- Usually there are two lines in table, one to cell, other to silhouette the table it self. Default is `collapse`.

**Color**
- The color of the line the table

**Text to the Table**
- Description to the table.
- All tables will be numbered

**Footer**
- If the last line of the table is a footer, this argument must be `True`.

`Prints such a string:`

![Table](https://github.com/dbranquinho/pywpb/readme_files/table_example.png)

<br>
<hr>
<br>

#### **Incorporate YouTube Videos**

This functionality lets you embed a YouTube video player on your website and control the player using JavaScript.

Using the API's JavaScript functions, you can queue videos for playback; play, pause, or stop those videos; adjust the player volume; or retrieve information about the video being played. You can also add event listeners that will execute in response to certain player events, such as a player state change.

```python
from pywpb import pywpb as wpb

filename = 'test'

h = wpb.header()
b = wpb.body()

b.youtube(video_id='rqz-sutSH0c', url='https://www.youtube.com/iframe_api')

i = wpb.wpIO()
i.write_file(filename,h,b)
i.preview(filename)
```

`Prints such a string HTML5:`

```html
<iframe width="320" height="240" 
            src="https://www.youtube.com/embed/rqz-sutSH0c" 
            frameborder="0" allow="accelerometer; autoplay; 
            clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
        </iframe>

        <script>
        var tag = document.createElement('script');

        tag.src = "https://www.youtube.com/iframe_api";
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        var player;
        function onYouTubeIframeAPIReady() {
            player = new YT.Player('player', {
            height: '240',
            width: '320',
            videoId: 'rqz-sutSH0c',
            events: {
                'onReady': onPlayerReady,
                'onStateChange': onPlayerStateChange
            }
            });
        }

        function onPlayerReady(event) {
            event.target.playVideo();
        }

        var done = false;
        function onPlayerStateChange(event) {
            if (event.data == YT.PlayerState.PLAYING && !done) {
            setTimeout(stopVideo, 6000);
            done = true;
            }
        }
        function stopVideo() {
            player.stopVideo();
        }
        </script>
```
<hr>

#### Lists

Lists allow developers to group a set of related items in lists. We have tree types of lists as follow.

**Unordered List**

The list items will be marked with bullets (small black circles) by default.


```python
from pywpb import pywpb as wpb

filename = 'test'

h = wpb.header()
b = wpb.body()

b.ulist(header="Header text to unordered list", itens=["item x", 'item y','item z'])
b.olist(header="Header text to ordered list", itens=["item 1", 'item 2','item 3'])
b.dlist(header="Header text to description list", 
        itens=[["desc 1", 'item 1','item 2','item 3'],
               ["desc 2", 'item a','item b']])
               
i = wpb.wpIO()
i.write_file(filename,h,b)
i.preview(filename)
```


### **wpIO (web page input and output)**

This method used to create an environment ways to input and output to your page created.

`sintax`:
```python
from pywpb import pywpb as wpb

i = wpb.wpIO()
```

There are no arguments to pass, but you will use the methods of that class.

<hr>

This module used to input and output all this that you create using pywpb. The Methods are:

**Print Page**

If you want to see how your page was built, this method will show you all HTML tags in your file with text output.

`sintax`:
```python
from pywpb import pywpb as wpb

p = wpb.creator('en')
b = wpb.body()

print_page(self, page=p, body=b, cfg_css=False):
```

If you have been calling commands that require CSS tags, then the `css_cfg` argument should be filled with True, but we will see that later.

<hr>

**Load File**
If you have a big text file to write on you page, this method is a best way to do this. After loaded, you can use the `text` to change colors of some words on the texto or put some words in bold or italic style.

You must write text on you page using `w_text` method.

`sintax`:
```python
from pywpb import pywpb as wpb

i = wpbnb.wpIO()
text = i.load_text('path/file.txt')
```

<hr>

`enjoi!`
