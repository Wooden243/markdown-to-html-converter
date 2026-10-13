import sys
import markdown

command = sys.argv[0]
input_path = sys.argv[1]
output_path = sys.argv[2]


if command == "md_to_html.py":
   with open(input_path, "r", encoding="utf-8") as file:
      contents = file.read()
      html = markdown.markdown(contents)

   with open(output_path, "w", encoding="utf-8") as file:
      file.write(html)


