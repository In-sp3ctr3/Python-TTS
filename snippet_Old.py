"""
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="upload" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    <form action="text" method=post enctype=multipart/form-data>
      <p><input type=text name=text>
         <input type=submit value=Upload>
    </form>
    <p>%s</p>
    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],)) 
    