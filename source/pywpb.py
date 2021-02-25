import pandas as pd
import numpy as np
import os
import webbrowser
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import datetime
import pkg_resources

class header:
    def __init__(self, charset='utf-8', 
                 page_size=[21.0, 29.7, 2.0],
                 margin=[0.25, 115],
                 background='transparent',
                 title='Neublis Page without Title',
                 set_logo=False,
                 table_width=100,
                 table_cellpadding1=4,
                 table_cellpadding2=0,
                 page_break_before='always',
                 col_width=128,
                 valign="top",
                 td_width=50,
                 td_border_top=1,
                 td_border_bottom=1,
                 td_border_left=1,
                 td_border_right=1,
                 td_padding_top=0.1,
                 td_padding_bottom=0.1,
                 td_padding_left=0.1,
                 td_padding_right=0,
                 logo_url_image='none',
                 name_image='none',
                 width_image=75,
                 height_image=35,
                 border_image=0,
                 text_width=50,
                 text_border=1,
                 text_padding=0.1,
                 text_logo='none'):
                 
        resource_package = __name__
        resource_path = '/'.join(('templates', 'templates.dat'))
        filepath = pkg_resources.resource_filename(resource_package, resource_path)
        self.df_template = pd.read_csv(filepath, sep=';')

        self.header = wpIO.read_template(self, file='header')
        self.header = self.header.replace('{{charset}}', charset)
        self.header = self.header.replace('{{dt_created}}', datetime.datetime.now().strftime('%Y/%m/%dT%H:%M:%S'))
        self.header = self.header.replace('{{page_size1}}', str(page_size[0]))
        self.header = self.header.replace('{{page_size2}}', str(page_size[1]))
        self.header = self.header.replace('{{page_size3}}', str(page_size[2]))
        self.header = self.header.replace('{{margin1}}', str(margin[0]))
        self.header = self.header.replace('{{margin2}}', str(margin[1]))
        self.header = self.header.replace('{{background}}', background)
        self.header = self.header.replace('{{title}}', title)

        if set_logo:
            self.logo = wpIO.read_template(self, file='logo')
            self.logo = self.logo.replace('{{table_width}}', str(table_width))
            self.logo = self.logo.replace('{{table_cellpadding1}}', str(table_cellpadding1))
            self.logo = self.logo.replace('{{table_cellpadding2}}', str(table_cellpadding2))
            self.logo = self.logo.replace('{{page_break_before}}', page_break_before)
            self.logo = self.logo.replace('{{col_width}}', str(col_width))
            self.logo = self.logo.replace('{{valign}}', valign)
            self.logo = self.logo.replace('{{td_width}}', str(td_width))
            self.logo = self.logo.replace('{{td_border_top}}', str(td_border_top))
            self.logo = self.logo.replace('{{td_border_left}}', str(td_border_left))
            self.logo = self.logo.replace('{{td_border_right}}', str(td_border_right))
            self.logo = self.logo.replace('{{td_border_bottom}}', str(td_border_bottom))
            self.logo = self.logo.replace('{{td_padding_bottom}}', str(td_padding_bottom))
            self.logo = self.logo.replace('{{td_padding_left}}', str(td_padding_left))
            self.logo = self.logo.replace('{{td_padding_right}}', str(td_padding_right))
            self.logo = self.logo.replace('{{logo_url_image}}', logo_url_image)
            self.logo = self.logo.replace('{{name_image}}', name_image)
            self.logo = self.logo.replace('{{valign}}', valign)
            self.logo = self.logo.replace('{{width_image}}', str(width_image))
            self.logo = self.logo.replace('{{height_image}}', str(height_image))
            self.logo = self.logo.replace('{{text_width}}', str(text_width))
            self.logo = self.logo.replace('{{text_border}}', str(text_border))
            self.logo = self.logo.replace('{{text_padding}}', str(text_padding))
            self.logo = self.logo.replace('{{text_logo}}', str(text_logo))
            self.header = self.header + self.logo
        else:
            self.header = self.header
        
        if not os.path.exists('images'):
            os.mkdir('images')
        ct_img = len(os.listdir('images'))
        if ct_img > 0:
            files = os.listdir('images')
            for filename in files:
                os.remove('images/' + filename)

class body:
    def __init__(self, margin=0, line=100, 
                 link='#000080', vlink='#800000',
                 lang='eng'): 

        resource_package = __name__
        resource_path = '/'.join(('templates', 'templates.dat'))
        filepath = pkg_resources.resource_filename(__name__, resource_path)
        self.df_template = pd.read_csv(filepath, sep=';')

        self.body = wpIO.read_template(self, 'body')      
        self.body = self.body.replace('{{margin}}', str(margin))
        self.body = self.body.replace('{{line}}', str(line))
        self.body = self.body.replace('{{link}}', link)
        self.body = self.body.replace('{{vlink}}', vlink)
        self.body = self.body.replace('{{lang}}', lang)

        self.cTab = 2  # indentation control tab
        self.ct_tbl = 0 # number of tables created

    # set tab control for tags around
    def config_tab(self, nr=0):
        self.cTab = self.cTab + nr
        if self.cTab < 0:
            self.cTab = 0
        text_tab = ''
        for i in range(self.cTab):
            text_tab = text_tab + '\t'
        return(text_tab)

    # headings
    def h(self, text='Headings have no text', 
                size=5, background='white', 
                align='left', color='black', shadow=False):

        if align not in ['center', 'left', 'right', 'justify']:
            raise ValueError('align %s not permited' % align)
        else:
            self.headings = wpIO.read_template(self, 'h')
            self.headings = self.headings.replace('{{size}}', str(size))
            self.headings = self.headings.replace('{{background}}', background)
            self.headings = self.headings.replace('{{text}}', text)
            self.headings = self.headings.replace('{{align}}', align)
            self.headings = self.headings.replace('{{color}}', color)
            
            self.body = self.body + self.config_tab() + self.headings 

    def color_text(self, text='no text provided', color='black'):
        self.text = wpIO.read_template(self, 'color_text')
        self.text = self.text.replace('{{text}}', text)
        self.text = self.text.replace('{{color}}', color)
        self.body = self.body + self.config_tab() + self.text 

    def w_text(self, text='no text provided', line_feed=1):
        self.body = self.body + self.config_tab() + text 
        for i in range(line_feed):
            self.body = self.body + '<BR>'
        self.body = self.body + '\n'

    def change_text_color(self, color='black',text='no text provided',
                                text_to='provided'):
        new_text = text.replace(text_to,'<span style="color:' + color + '">' + text_to + ' </span>')
        return(new_text)

    def bold_text(self, text='no text provided',
                        text_to='no text to was provided'):
        text = '\n' + self.config_tab() + text                        
        new_text = text.replace(text_to,' <strong>' + text_to + ' </strong>')
        return(new_text)

    def italic_text(self, text='no text provided',
                        text_to='no text to was provided'):
        text = '\n' + self.config_tab() + text                        
        new_text = text.replace(text_to,' <i>' + text_to + ' </i>')
        return(new_text)

    def hline(self, height=1, border=0, color='gray', background='gray'):
        self.text = wpIO.read_template(self, 'hline')
        self.text = self.text.replace('{{height}}', str(height))
        self.text = self.text.replace('{{border}}', str(border))
        self.text = self.text.replace('{{color}}', color)
        self.text = self.text.replace('{{background}}', background)
        self.body = self.body + self.config_tab() + self.text 


    def w_table(self, data="none", border=1, align='left', 
                      collapse='collapse', color='black', 
                      alt_text='no text provided',
                      foot=False):

        if foot:
            sum_shape = -1
        else:
            sum_shape = 0

        if str(type(data)) != "<class 'str'>":
            self.tableh = wpIO.read_template(self, 'tableh')
            self.tableh = self.tableh.replace('{{align}}', align)
            self.tableh = self.tableh.replace('{{collapse}}', collapse)
            self.tableh = self.tableh.replace('{{border_size}}', str(border))
            self.tableh = self.tableh.replace('{{border_color}}', color)
            self.tablef = wpIO.read_template(self, 'tablef')
            self.tableh = self.tableh.replace('{{alt_text}}', alt_text)
            self.ct_tbl += 1
            self.tableh = self.tableh.replace('{{ct_tbl}}', str(self.ct_tbl))
        else:
            raise ValueError('No dataframe provided to write table, I need one')

        self.body = self.body + self.tableh
        self.theadh = wpIO.read_template(self, 'table_theadh')
        self.theadb = wpIO.read_template(self, 'table_theadb')
        self.theadf = wpIO.read_template(self, 'table_theadf')
        self.tbodyh = wpIO.read_template(self, 'table_tbodyh')
        self.tbodyb = wpIO.read_template(self, 'table_tbodyb')
        self.tbodyf = wpIO.read_template(self, 'table_tbodyf')

        # building table head 
        self.body = self.body + self.theadh
        for col_names in data.columns:
            self.field = self.theadb.replace('{{field}}', col_names)
            self.body = self.body + self.config_tab() + self.field
        self.body = self.body + self.theadf

        # building table body
        self.body = self.body + self.tbodyh
        self.config_tab(2)
        for i in range(data.shape[0] + sum_shape):
            self.body = self.body + self.config_tab() + '<tr>\n'
            for j in range(data.shape[1]):
                self.field = self.tbodyb.replace('{{field}}', str(data.iloc[i][j]))
                self.body = self.body + self.config_tab() + self.field
            self.body = self.body + self.config_tab() + '</tr>\n'
        self.body = self.body + self.tbodyf
        self.config_tab(-2)
        # building table foot
        if foot:
            self.tfooth = wpIO.read_template(self, 'table_tfooth')
            self.tfootb = wpIO.read_template(self, 'table_tfootb')
            self.tfootf = wpIO.read_template(self, 'table_tfootf')
            i = data.shape[0] -1
            self.body = self.body + self.tfooth
            for j in range(data.shape[1]):
                self.field = self.tfootb.replace('{{field}}', str(data.iloc[i][j]))
                self.body = self.body + self.config_tab() + self.field
            self.body = self.body + self.tfootf
        else:
            self.body = self.body + self.config_tab() + self.tablef


    def w_image(self, image='none', width=350, 
                      height=350, alt_text='no alt text was provided'):

        if str(type(image)) == "<class 'str'>":
            raise ValueError('No image provided to create graph, I need one')

        if not os.path.exists('images'):
            os.mkdir('images')
        ct_img = len(os.listdir('images')) + 1
        plt.savefig('images/img_' + str(ct_img) + '.png')
        
        self.tag_image = wpIO.read_template(self, 'image')
        self.tag_image = self.tag_image.replace('{{height}}', str(height))
        self.tag_image = self.tag_image.replace('{{width}}', str(width))
        self.tag_image = self.tag_image.replace('{{ct_img}}', str(ct_img))
        self.tag_image = self.tag_image.replace('{{alt_text}}', alt_text)
        self.body = self.body + self.tag_image

    def w_footer(self, header='This page was built with Neublis', 
                       link_email='delermando@gmail.com', name_email='Delermando', 
                       align='center', padding=3,
                       background_color='gray',
                       color='black'):
        
        self.tag_footer = wpIO.read_template(self, 'footer')
        self.tag_footer = self.tag_footer.replace('{{header}}', header)
        self.tag_footer = self.tag_footer.replace('{{link_email}}', link_email)
        self.tag_footer = self.tag_footer.replace('{{name_email}}', name_email)
        self.tag_footer = self.tag_footer.replace('{{align}}', align)
        self.tag_footer = self.tag_footer.replace('{{background-color}}', background_color)
        self.tag_footer = self.tag_footer.replace('{{color}}', color)
        self.tag_footer = self.tag_footer.replace('{{padding}}', str(padding))
        self.body = self.body + self.tag_footer

    def page_header(self, title='This title was built with Neublis', 
                    sub_title='Author: Delermando', size=4):
        
        self.page_header_tag = wpIO.read_template(self, 'page_header')
        self.page_header_tag = self.page_header_tag.replace('{{title}}', title)
        self.page_header_tag = self.page_header_tag.replace('{{sub_title}}', sub_title)
        self.page_header_tag = self.page_header_tag.replace('{{size}}', str(size))
        self.body = self.body + self.page_header_tag

    def show_video(self, width=320, height=240, url='none', type='mp4'):

        if url == 'none':
            raise ValueError('No valid URL, I need one')

        self.video_tag = wpIO.read_template(self, 'video')
        self.video_tag = self.video_tag.replace('{{width}}', str(width))
        self.video_tag = self.video_tag.replace('{{height}}', str(height))
        self.video_tag = self.video_tag.replace('{{url}}', url)
        self.video_tag = self.video_tag.replace('{{type}}', type)
        self.body = self.body + self.video_tag

    def youtube(self, width=320, height=240, video_id='none', url='none'):

        if url == 'none':
            raise ValueError('No valid URL, I need one')

        self.video_tag = wpIO.read_template(self, 'youtube')
        self.video_tag = self.video_tag.replace('{{width}}', str(width))
        self.video_tag = self.video_tag.replace('{{height}}', str(height))
        self.video_tag = self.video_tag.replace('{{url}}', url)
        self.video_tag = self.video_tag.replace('{{video_id}}', video_id)
        self.body = self.body + self.video_tag

    def w_frame(self, margin_botton=0, line_height=100, align='left',
                width=260, border=1, solid='#000000', padding=0.15, 
                background='#ffffff', ncols=1, gutter=19, frame_id='none',
                text_line='none'):
        self.frame_tag = wpIO.read_template(self, 'frame')
        self.frame_tag = self.frame_tag.replace('{{margin_botton}}', str(margin_botton))
        self.frame_tag = self.frame_tag.replace('{{line_height}}', str(line_height))
        self.frame_tag = self.frame_tag.replace('{{align}}', align)
        self.frame_tag = self.frame_tag.replace('{{width}}', str(width))
        self.frame_tag = self.frame_tag.replace('{{border}}', str(border))
        self.frame_tag = self.frame_tag.replace('{{padding}}', str(padding))
        self.frame_tag = self.frame_tag.replace('{{background}}', str(background))
        self.frame_tag = self.frame_tag.replace('{{ncols}}', str(ncols))
        self.frame_tag = self.frame_tag.replace('{{ncols}}', str(ncols))
        self.frame_tag = self.frame_tag.replace('{{gutter}}', str(gutter))
        self.frame_tag = self.frame_tag.replace('{{frame_id}}', frame_id)
        self.frame_tag = self.frame_tag.replace('{{text_line}}', str(text_line))
        self.body = self.body + self.frame_tag

    def ulist(self, header="Header text to list", itens=["item 1", 'item 2','item 3']):
        
        self.Lines = wpIO.read_template(self, 'ulist')
        ct_line = 0
        ct_itens = len(itens)
        text = ""
        self.w_text(text=header, line_feed=0)
        for line in self.Lines.splitlines():
            if ct_line == 0:
                ct_line = ct_line + 1
                text = text + line + '\n'
                continue      
            if ct_line == 1:
                for i in range(ct_itens):
                    text = text + line.replace('{{item}}', itens[i]) + '\n'
                ct_line = ct_line + 1
                continue      
            if ct_line == 2:
                text = text + line + '\n'
                break
        self.body = self.body + text

    def olist(self, header="Header text to list", itens=["item 1", 'item 2','item 3']):
        
        self.Lines = wpIO.read_template(self, 'olist')
        ct_line = 0
        ct_itens = len(itens)
        text = ""
        self.w_text(text=header, line_feed=0)
        for line in self.Lines.splitlines():
            if ct_line == 0:
                ct_line = ct_line + 1
                text = text + line + '\n'
                continue      
            if ct_line == 1:
                for i in range(ct_itens):
                    text = text + line.replace('{{item}}', itens[i]) + '\n'
                ct_line = ct_line + 1
                continue      
            if ct_line == 2:
                text = text + line + '\n'
                break
        self.body = self.body + text

    def dlist(self, header="Header text to description list", 
                    itens=[["desc 1", 'item 1','item 2','item 3'],
                           ["desc 2", 'item a','item b']]):
        
        file_text = wpIO.read_template(self, 'dlist')
        lines = file_text.splitlines()
        self.w_text(text=header, line_feed=0)
        text = lines[0]
        for i in range(len(itens)):
            text = text + lines[1].replace('{{description}}', itens[i][0]) + '\n'
            for j in range(1,len(itens[i])):
                text = text + lines[2].replace('{{item}}', itens[i][j]) + '\n'
        text = text + lines[3]
        self.body = self.body + text

    def w_forms(self, form_id='none',text='none', url_privacy='none', bus_name='none', submit='none'):
        if form_id == 'none':
            raise ValueError('No Form ID was provided, I need one')
        if url_privacy == 'none':
            raise ValueError('No URL to privacy was provided, I need one to LGPD conformance')
        if bus_name == 'none':
            raise ValueError('No Business Name was provided, I need one to submit form')
        if submit == 'none':
            raise ValueError('No URL to submit was provided, I need one to submit form')
        if text == 'none':
            raise ValueError('No Text to form was provided, I need one to Create form')
        
        self.form_tag = wpIO.read_template(self, form_id)
        self.form_tag = self.form_tag.replace('{{url_privacy}}', url_privacy) 
        self.form_tag = self.form_tag.replace('{{bus_name}}', bus_name) 
        self.form_tag = self.form_tag.replace('{{text}}', text) 
        self.form_tag = self.form_tag.replace('{{submit}}', submit) 
        
        self.body = self.body + self.form_tag

    def w_tabs(self, title_tab='none', text_tab='none', tab_name='none', text_tab_name='none'):
        if title_tab == 'none':
            raise ValueError('No title_tab was provided, I need one')
        if text_tab == 'none':
            raise ValueError('No text_tab was provided, I need one')
        if tab_name == 'none':
            raise ValueError('No tab_name was provided, I need one')
        if text_tab_name == 'none':
            raise ValueError('No text_tab_name was provided, I need one')
        
        if len(tab_name) != len(text_tab_name):
            raise ValueError('Different size between tab_name and Text_tab_name')

        self.tab_tag = wpIO.read_template(self, 'tab1')
        self.tab_tag = self.tab_tag.replace('{{title_tab}}', title_tab) 
        self.tab_tag = self.tab_tag.replace('{{text_tab}}', text_tab) 
        self.body = self.body + self.tab_tag

        for i in range(len(tab_name)):
            self.tab_tag = wpIO.read_template(self, 'tab2')
            self.tab_tag = self.tab_tag.replace('{{tab_name}}', tab_name[i]) 
            self.body = self.body + self.tab_tag

        for i in range(len(tab_name)):
            self.tab_tag = wpIO.read_template(self, 'tab3')
            self.tab_tag = self.tab_tag.replace('{{tab_name}}', tab_name[i]) 
            self.tab_tag = self.tab_tag.replace('{{text_tab_name}}', text_tab_name[i]) 
            self.body = self.body + self.tab_tag

        self.tab_tag = wpIO.read_template(self, 'tab4')
        self.body = self.body + self.tab_tag


class wpIO:

    def __init__(self):
        resource_package = __name__
        resource_path = '/'.join(('templates', 'templates.dat'))
        filepath = pkg_resources.resource_filename(resource_package, resource_path)
        self.df_template = pd.read_csv(filepath, sep=';')

    def parse(self, page='none', body='none', cfg_css='none'):
        
        text = ''

        if str(type(page)) != "<class 'str'>":
            text = page.header

        if str(type(body)) != "<class 'str'>":
            text = text + body.body

        return(text)

    def print_page(self, page='none', body='none', cfg_css='none'):
        text = self.parse(page, body, cfg_css)
        print(text)

    def read_template(self, file):
        resource_package = __name__
        file_read = self.df_template[self.df_template['template'] == file]['file']
        file_read = file_read.to_string().split(' ')[-1]
        resource_path = '/'.join(('templates', file_read))
        filepath = pkg_resources.resource_filename(resource_package, resource_path)
        try:
            text_file = open(filepath,"r")
        except:
            raise ValueError('Template not found!!!')

        Lines = text_file.readlines()
        str = ""
        for line in Lines:
            str = str + line
        text_file.close()        
        return(str)

    def write_file(self, filename, page='none', body='none', cfg_css='none', mode='w+'):
        text = self.parse(page, body, cfg_css)
        if str(type(body)) != "<class 'str'>":
            close_body = wpIO.read_template(self, 'close_body') 
            text = text + close_body
        if str(type(page)) != "<class 'str'>":        
            close_page = wpIO.read_template(self, 'close_page') 
            text = text + close_page
        file2write = filename + '.html'
        file = open(file2write,mode) 
        file.write(text)
        file.close()

    def preview(self, filename):
        webbrowser.open('file://' + os.path.realpath(filename) + '.html')

    def load_text(self, file):
        text_file = open(file,'r')
        Lines = text_file.readlines()
        str = ""
        for line in Lines:
            str = str + line
        text_file.close()        
        return(str)
