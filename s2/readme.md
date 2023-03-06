# Setting up
TBA

# curl
note that nFile could be many files in folders, if the mutation could recieve multiple files

```bash
curl --request POST \
  --url http://127.0.0.1:8000/myapp/graphql/ \
  --form 'operations={"query":"mutation MyMutation($file: Upload!) {\n  createAuthor(data: {name: \"my great author\", image: $file}) {\n    id\n  }\n}","variables>
  --form 'map={ "nFile": ["variables.file"] }' \
  --form nFile=@author.png
```
# Mutation Author
```bash
source make_author.sh
```