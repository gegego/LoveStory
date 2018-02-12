import React, { PureComponent } from 'react';
import {
  Button,
  Card,
  CardTitle,
  CardText,
  Media,
  MediaOverlay,
} from 'react-md';
import StoryText from './storytext'
// import { QUOTATION_MARK } from 'constants/unicode';

// import { randomImage } from 'utils/random';

// const nature = randomImage({ width: 600, height: 337, section: 'nature' });
const cards = [
  {
    id: "0",
    user_info: "jack",
    img_url: '/static/google.png',
    story_text: 'Starry Night'
  },
  {
    id: "1",
    user_info: "mary",
    img_url: '/static/google.png',
    story_text: 'Wheat Field with Cypresses'
  },
  {
    id: "2",
    user_info: "peter",
    img_url: '/static/google.png',
    story_text: 'Bedroom in Arles'
  }
]



function CardlistX(props) {
  const cards = props.cards;
  const carditems = cards.map((card) =>
    <Card key={card.id} className="cards__example md-cell md-cell--6 md-cell--8-tablet">
    <Media><img src={card.img_url} /></Media>
    <CardText><p>{card.story_text}</p>
    <StoryText cardinfo={card}  />
    </CardText>
    </Card>
  );
  return (
    <div className="md-grid">
      {carditems}
    </div>
  );
}

class StoryList extends PureComponent {
  state = {CardList: []}

  componentWillMount() {

    fetch('http://192.168.0.101:5000/storys', {
      method: 'GET',
    }).then((response) => {
      response.json().then((body) => {
        console.log(body);
        this.setState({CardList:body})
      });
    });
  }

  render() {
    return (
      <CardlistX cards={this.state.CardList} />
    );
  }
}
export default StoryList;
