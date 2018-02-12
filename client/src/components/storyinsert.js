import React, { PureComponent } from 'react';
import {
  Button,
  DialogContainer,
  Divider,
  TextField,
  Toolbar,
  Media,
} from 'react-md';
import ImageUpload from './fileupload'

export default class WriteStory extends PureComponent {

  render() {
    return (
      <ImageUpload />
    );
  }
}
