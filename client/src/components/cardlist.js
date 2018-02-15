import React, { PureComponent } from 'react';
import {
  Card,
  CardText,
  Media,
} from 'react-md';
import StoryText from './storytext'

function CardlistX(props) {
  const cards = props.cards;
  const carditems = cards.map((card) =>
    <Card key={card.id} className="cards__example md-cell md-cell--6 md-cell--8-tablet">
    <Media><img src={'/static/story_image/'+card.img_url} alt='' /></Media>
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

    fetch('http://45.77.125.230/storys', {
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
