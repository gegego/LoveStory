import React, { PureComponent } from 'react';
import {
  Button,
  DialogContainer,
  Divider,
  Toolbar,
  Paper,
  Media,
} from 'react-md';

export default class StoryText extends PureComponent {
  // console.log(this.props);
  title = this.props.cardinfo.user_info;
  img = this.props.cardinfo.img_url;
  text = this.props.cardinfo.story_text;

  state = { visible: false };
  show = (e) => {
    this.setState({ visible: true });
  };

  hide = () => {
    this.setState({ visible: false });
  };

  render() {
    const { visible } = this.state;

    return (
      <div>
        <Button raised onClick={this.show} aria-controls="simple-full-page-dialog">
          Show Details
        </Button>
        <DialogContainer
          id="simple-full-page-dialog"
          visible={visible}
          fullPage
          onHide={this.hide}
          aria-labelledby="simple-full-page-dialog-title"
        >
          <Toolbar
            fixed
            colored
            title={this.title}
            titleId="simple-full-page-dialog-title"
            nav={<Button icon onClick={this.hide}>close</Button>}
          />
          <section className="md-toolbar-relative">
            <Media>
              <img src={this.img} alt='' />
            </Media>
            <Divider />
            <div className="papers__container">
              <Paper
                  className="papers__example"
                >
                  <p className="md-color--secondary-text">{this.text}</p>
              </Paper>
            </div>
          </section>
        </DialogContainer>
      </div>
    );
  }
}
