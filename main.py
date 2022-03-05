import re
import requests

def get_tag(tag_name,html_text):
  tag_ary = re.findall("<" + tag_name + f'[^>]+>',html_text)
  return tag_ary

def attr_value(attr_name,html_text):
  reg_text = attr_name + f'=""?([^\s""]+)""?'
  type_attr_ary = re.findall(reg_text,html_text)
  return type_attr_ary

def form_to_dict(html_text):
  form_data ={}
  html_tag_ary = get_tag('input',html_text)
  for html_tag in html_tag_ary:
    type_attr = attr_value("type",html_tag)
    name_attr = attr_value("name",html_tag)
    value_attr = attr_value("value",html_tag)
    if len(name_attr) > 0 and len(name_attr) > 0 and len(value_attr) > 0:
      if "text" in type_attr or "hidden" in type_attr or "password" in type_attr:
        form_data[name_attr[0]] = value_attr[0]
  
  return form_data


if __name__ == '__main__':

  html_text = f'<input type="text">'
  html_text = html_text + f'<input type="text" name="test" value="Hello,World">'
  html_text = html_text + f'<input type="hidden" name="test2" value="sample">'

  html_text = requests.get("https://qiita.com/login").text
  form_data = form_to_dict(html_text)
  print(form_data)
