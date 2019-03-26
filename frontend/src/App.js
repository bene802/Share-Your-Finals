import React, { Component } from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import PostList from "./components/PostList";
import Intro from "./components/Intro";

class App extends Component {
  state = {
    posts: [
      {
        id: 1,
        user_id: 1,
        author: "Mike",
        title: "title1",
        date: "2019-10-10",
        content: "Made by User1"
      },
      {
        id: 2,
        user_id: 1,
        author: "Mike",
        title: "title2",
        date: "2019-10-11",
        content: "Made by User1"
      },
      {
        id: 3,
        user_id: 2,
        author: "Jack",
        title: "title3",
        date: "2019-09-10",
        content: "Made by User2"
      }
    ]
  };
  render() {
    return (
      <React.Fragment>
        <Navbar />
        <div className="container">
          <Intro />
          <main className="container">
            <PostList posts={this.state.posts} />
          </main>
        </div>
      </React.Fragment>
    );
  }
}

export default App;
