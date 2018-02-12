/* Fixed.jsx */
import React, { PureComponent } from 'react';
import {
  Button,
  DialogContainer,
  Divider,
  TextField,
  Toolbar,
  Media,
  FontIcon,
  SVGIcon
 } from 'react-md';
 import {
   BrowserRouter as Router,
   Route,
   Link,
   Redirect,
   withRouter,
   Switch
 } from "react-router-dom";
 import StoryList from './cardlist';
 import StoryInsert from './storyinsert'
// import Recent from './Recent';


const WriteIcon = props => (
  <SVGIcon {...props}>
    <path d="M1.227 4.509c0-1.812 1.469-3.281 3.281-3.281 0.739 0 1.42 0.244 1.969 0.656l1.313 1.312-4.594 4.594-1.313-1.313c-0.412-0.548-0.656-1.23-0.656-1.969zM16.321 20.915l5.906 1.313-1.313-5.906-12.141-12.141-4.594 4.594 12.141 12.141zM8.684 7.552l9.188 9.188-1.131 1.131-9.187-9.188 1.131-1.131z"></path>
  </SVGIcon>
);

const HomeIcon = props => (
  <SVGIcon {...props}>
  <path d="M23.549 13.237l-11.591-8.997-11.591 8.997v-3.668l11.591-8.997 11.591 8.997zM20.651 12.91v8.693h-5.796v-5.796h-5.796v5.796h-5.795v-8.693l8.693-6.52z"></path>
  </SVGIcon>
);

class Main extends PureComponent {
  state = { idx : 1, icon: <WriteIcon /> };

  show = (e) => {
    const {idx} = this.state;
    // console.log(idx);
    if(idx == 1){
      this.setState({idx : 2, icon: <HomeIcon />});
      this.props.history.push('/story');
    }
    else{
      this.setState({idx : 1, icon: <WriteIcon />});
      this.props.history.push('/');
    }
  };
  render() {
    const {idx, icon} = this.state;
    return (
      <div>
        <Toolbar
          fixed
          colored
          title='爱的博物馆'
        />
        <div className="md-toolbar-relative">
          <Switch>
            <Route path="/" exact component={StoryList} />
            <Route path="/story" component={StoryInsert} />
          </Switch>
        </div>
        <Button onClick={this.show} fixed className='positionInBottom' floating svg secondary>
          {icon}
        </Button>
      </div>
    );
  }
}

export default withRouter(Main);
