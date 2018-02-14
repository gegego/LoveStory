import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from werkzeug.utils import secure_filename
import werkzeug
from flask_sqlalchemy import SQLAlchemy
import uuid

application = Flask(__name__)
CORS(application)
api = Api(application)

UPLOAD_FOLDER = '../client/public/static/story_image'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/LoveStory'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

# Create our database model
class LoveStory(db.Model):
    __tablename__ = "lovestory"
    id = db.Column(db.Integer, primary_key=True)
    user_info = db.Column(db.String(80))
    img_url = db.Column(db.String(500))
    story_text = db.Column(db.String(1000))
    satus = db.Column(db.Integer)

    def __init__(self, user_info, img_url, story_text):
        self.user_info = user_info
        self.img_url = img_url
        self.story_text = story_text
        self.status = 1

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class StoryAPI(Resource):
    def get(self, story_id):
        story = db.session.query(LoveStory).filter_by(id=story_id).first()
        if not story:
            return {'message': 'Not found'}, 404
        return {story_id: story}

    def post(self, story_id):
        story = db.session.query(LoveStory).filter_by(id=story_id).first()
        if not story:
            return {'message': 'Not found'}, 404

        story.img_url = request.form['img_url']
        story.story_text = request.form['story_text']
        db.session.commit()
        return {story_id: story}

class StoryListAPI(Resource):
    def get(self):
        return [{'id': story.id,'user_info': story.user_info, \
                'img_url': story.img_url, 'story_text': story.story_text\
                } for story in db.session.query(LoveStory).all()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_info')
        parser.add_argument('img_url')
        parser.add_argument('story_text')
        args = parser.parse_args()
        if not 'user_info' in args or not 'img_url' in args or not 'story_text' in args:
            return {'message': 'Missing required parameters.'}, 400

        new_story = LoveStory(user_info=args['user_info'], img_url=args['img_url'], \
                            story_text=args['story_text'])
        db.session.add(new_story)
        db.session.commit()
        return {new_story.id: {'user_info': new_story.user_info, 'img_url': new_story.img_url,\
                'story_text': new_story.story_text}}, 201

class UploadImage(Resource):
    def post(self):
        # print('recived')
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.FileStorage, location='files')
        parse.add_argument('filename')
        parse.add_argument('user_info')
        parse.add_argument('story_text')
        args = parse.parse_args()

        imgfile = args['file']
        if not 'user_info' in args or not 'story_text' in args:
            return {'message': 'Missing required parameters.'}, 400

        # print(imgfile)
        # if file and allowed_file(file.filename):
            # From flask uploading tutorial
        filename = str(uuid.uuid4()) + secure_filename(imgfile.filename)
        imgfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_story = LoveStory(user_info=args['user_info'], img_url=filename, \
                            story_text=args['story_text'])
        db.session.add(new_story)
        db.session.commit()

        return {new_story.id: {'user_info': new_story.user_info, 'img_url': new_story.img_url,\
                'story_text': new_story.story_text}}


api.add_resource(StoryAPI, '/storys/<int:id>')
api.add_resource(StoryListAPI, '/storys')
api.add_resource(UploadImage, '/upload')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=5000)
