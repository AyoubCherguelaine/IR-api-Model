from model import model,vector
from model.document import doc,upload
from model.query import query
from model.model import similarity

text="""This is a built-in middleware function in Express. It parses incoming requests with JSON payloads and is based on body-parser.

Returns middleware that only parses JSON and only looks at requests where the Content-Type header matches the type option. This parser accepts any Unicode encoding of the body and supports automatic inflation of gzip and deflate encodings.

A new body object containing the parsed data is populated on the request object after the middleware (i.e. req.body), or an empty object () if there was no body to parse, the Content-Type was not matched, or an error occurred."""


d = doc(text)

qText = input("query : ")

qr = query(qText)

val = similarity.dice(d,qr)

print("dice : ",val)