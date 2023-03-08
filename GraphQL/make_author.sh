curl --request POST \
  --url http://127.0.0.1:8000/myapp/graphql/ \
  --form 'operations={"query":"mutation MyMutation($file: Upload!) {\n  createAuthor(data: {name: \"my great author\", image: $file}) {\n    id\n  }\n}","variables": { "file": null } }' \
  --form 'map={ "nFile": ["variables.file"] }' \
  --form nFile=@author.png
