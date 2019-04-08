#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

def rot13(usertext):
    k=len(usertext)
    encryp_text="" 
    for x in range(0,k):
         fac = ord(usertext[x])
         if (fac>=97 and fac<=109)or(fac>=65 and fac<=77):
             test = ord(usertext[x])+13 
             encryp_text+= chr(test)
         elif (fac>=110 and fac<=122) or (fac>=78 and fac<=90):
             test = ord(usertext[x])-13
             encryp_text+= chr(test)
         else:
             encryp_text+= chr(fac)  
    return encryp_text   
import os
import webapp2
import jinja2

template_dir= os.path.join(os.path.dirname('main.py'),'templates')                         
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))                              

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
   
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)    
        
    def render(self, template, **kw):
        self.write(self.render_str(template,**kw))
    
                          
class Mainpage(Handler):
    def get(self):
        self.render("form13.html")
   

class rotHandler(Handler):
    def post(self):
        usertext = self.request.get('text')
        text = rot13(usertext)
        self.render("rot13.html", text=text)   

app=webapp2.WSGIApplication([('/', Mainpage),
                            ('/rot13', rotHandler)
                            ],                                  
                           debug=True)

        

