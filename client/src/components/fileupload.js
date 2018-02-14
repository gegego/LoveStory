/* SimpleFileUpload.jsx */
import React, { PureComponent } from 'react';
import {
  Button,
  FileUpload,
  Media,
  MediaOverlay,
  CardTitle,
  TextField,
  Divider,
  DialogContainer,
  Card,
  CardText,
} from 'react-md';
import guid from 'uuid/v1';
import {
  withRouter
} from "react-router-dom";

import './_styles.scss';

class ImageUpload extends PureComponent {
  state = { file: null, image: '/static/upload.jpg', story_name: '', story_text:'', visible: false};
  constructor(props) {
    super(props)

    this.storySubmit = this.storySubmit.bind(this)
  }

  componentWillUnmount() {
    if (this.timeout) {
      clearTimeout(this.timeout);
    }
  }

  setFileUpload = (fileUpload) => {
    this.fileUpload = fileUpload;
  };

  setFile = (file) => {
    this.setState({ file });
  };

  abortUpload = () => {
    if (this.fileUpload) {
      this.fileUpload.abort();
    }

    this.setState({ file: null });
  };

  updateName = (name) => {
    this.setState({ story_name: name });
  };

  updateText = (text) => {
    this.setState({ story_text: text });
  };

  /**
   * This is triggered once a file has been successfully uploaded.
   *
   * @param {File} uploadedFile - the fully uploaded file. The properties
   *    of this object change depending on the browser, but normally
   *    the name, size, type, and lastModifiedDate are the same.
   * @param {String} uploadedData - This will be whatever the results of
   *    the upload was. So this could be the text in a file, a data-url
   *    for an image, or some other content for other file types.
   */
  handleLoad = (uploadedFile, uploadedData) => {
    const { name, size, type, lastModified } = uploadedFile;
    const file = {
      id: guid(),
      name,
      size,
      type,
      data: uploadedData,
      lastModified: new Date(lastModified),
    };
    let img;
    img = file.data;
    this.setState({ file: file, image: img });
  };

  storySubmit = (e) => {
    e.preventDefault();

    const data = new FormData(e.target);
    const file = data.get('file');
    if (!file || !file.name) {
      this.addToast('A file is required.');
      return;
    }
    data.append('user_info', this.state.story_name);
    data.append('story_text', this.state.story_text);
    // console.log(this.state);

    fetch('http://45.77.125.230/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        console.log(body);
      });
    });

    this.setState({ visible: true });
  }

  hide = () => {
    console.log('aasdfsdf');
    this.props.history.push('/')
    window.location.reload()
    this.setState({ visible: false });
  };

  render() {
    const { file, image, story_name, story_text, visible } = this.state;

    return (

      <div className="md-toolbar-relative">
      <form
        id="server-upload-form"
        ref={this.setForm}
        onSubmit={this.storySubmit}
        name="server-upload-form"
        className="file-inputs__upload-form"
      >
      <Card key='1' className="cards__example md-cell md-cell--6 md-cell--8-tablet">
        <Media>
          <img src={this.state.image} alt='' />
          <MediaOverlay>
            <FileUpload
              id="multiple-file-upload"
              multiple
              secondary
              accept="image/*"
              name="file"
              ref={this.setFileUpload}
              label="Select files"
              onLoadStart={this.setFile}
              onLoad={this.handleLoad}
            />
          </MediaOverlay>
        </Media>
        <Divider />
        <section>
          <TextField
            id="email-subject"
            placeholder="Name"
            value={story_name}
            block
            paddedBlock
            onChange={this.updateName}
            maxLength={80}
          />
          <Divider />
          <div className="papers__container">
            <TextField
              id="story-body"
              placeholder="Story Text"
              block
              rows={8}
              value={story_text}
              paddedBlock
              maxLength={1000}
              onChange={this.updateText}
              errorText="Max 1000 characters."
            />
          </div>
        </section>
        </Card>
        <Button raised primary type="submit">
           SUBMIT
         </Button>
         </form>
         <DialogContainer
          id="simple-full-page-dialog"
          visible={visible}
          fullPage
          onHide={this.hide}
          aria-labelledby="simple-full-page-dialog-title"
        >
          <Card className="md-block-centered">
            <Media>
              <img src={this.state.image} alt='' />
              <MediaOverlay>
                <CardTitle title={this.state.story_name} />
              </MediaOverlay>
            </Media>
            <Divider />
            <CardText>
              <p>{this.state.story_text}</p>
            </CardText>
          </Card>
          <Button raised primary onClick={this.hide}>
             Close
           </Button>
        </DialogContainer>
      </div>

    );
  }
}

export default withRouter(ImageUpload);
