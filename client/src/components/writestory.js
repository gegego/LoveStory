import React, { PureComponent } from 'react';
import {
  Button,
  DialogContainer,
  Divider,
  TextField,
  Toolbar,
  Media,
} from 'react-md';

export default class WriteStory extends PureComponent {

  render() {
    return (
      <section className="md-toolbar-relative">
        <TextField
          id="email-subject"
          placeholder="Name"
          block
          paddedBlock
          maxLength={80}
        />
        <Divider />
        <TextField
          id="story-body"
          placeholder="Story Text"
          block
          rows={4}
          paddedBlock
          maxLength={1000}
          errorText="Max 1000 characters."
        />
      </section>
    );
  }
}
