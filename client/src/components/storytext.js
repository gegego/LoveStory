import React, { PureComponent } from 'react';
import {
  Button,
  DialogContainer,
  Divider,
  TextField,
  Toolbar,
  Paper,
  Media,
} from 'react-md';

export default class StoryText extends PureComponent {
  // console.log(this.props);
  title = this.props.cardinfo.user_info;
  img = this.props.cardinfo.img_url;
  text = this.props.cardinfo.story_text;

  state = { visible: false, pageX: null, pageY: null };
  show = (e) => {
    // provide a pageX/pageY to the dialog when making visible to make the
    // dialog "appear" from that x/y coordinate
    let { pageX, pageY } = e;
    if (e.changedTouches) {
      pageX = e.changedTouches[0].pageX;
      pageY = e.changedTouches[0].pageY;
    }

    this.setState({ visible: true, pageX, pageY });
  };

  hide = () => {
    this.setState({ visible: false });
  };

  render() {
    const { visible, pageX, pageY } = this.state;

    return (
      <div>
        <Button raised onClick={this.show} aria-controls="simple-full-page-dialog">
          Show Details
        </Button>
        <DialogContainer
          id="simple-full-page-dialog"
          visible={visible}
          pageX={pageX}
          pageY={pageY}
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
              <img src={this.img} />
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
