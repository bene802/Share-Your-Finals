import React, { Component } from "react";
import Post from "./Post";

class PostList extends Component {
  render() {
    return (
      <div>
        {this.props.posts.map(post => (
          <Post key={post.id} post={post} />
        ))}
      </div>
    );
  }
}
export default PostList;
