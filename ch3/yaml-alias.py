import yaml

# 文字列でYAMLを定義
yaml_str = """
# 定義
color_def:
  - &color1 "#FF0000"
  - &color2 "#00FF00"
  - &color3 "#0000FF"

# エイリアスのテスト
color:
  title: *color1
  body: *color2
  link: *color3
"""

# YAMLを解析
data = yaml.load(yaml_str)

# エイリアスが展開されているかテスト
print("title=", data["color"]["title"])
print("body=", data["color"]["body"])
print("link=", data["color"]["link"])

