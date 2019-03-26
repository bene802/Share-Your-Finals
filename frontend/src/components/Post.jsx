import React, { Component } from "react";
import Button from "react-bootstrap/Button";

class Post extends Component {
  render() {
    return (
      <div className="card flex-md-row mb-4 box-shadow h-md-250">
        <div className="card-body d-flex flex-column align-items-start">
          <strong className="d-inline-block mb-2 text-primary">
            {this.props.post.author}
          </strong>
          <div className="mb-0">
            <div className="text-dark " href="#">
              <h3>{this.props.post.title}</h3>
            </div>
          </div>
          <div className="mb-1 text-muted">{this.props.post.date}</div>
          <p className="card-text mb-auto">{this.props.post.content}</p>
        </div>
        <span className="card-right flex-auto d-none d-md-block mr-2 mt-3">
          <button
            className="fas fa-edit btn btn-primary mr-2 mb-2"
            onClick={() => this.props.handleEditShow()}
          >
            {" "}
            Edit
          </button>
          <button className="fas fa-trash-alt btn btn-danger mb-2">
            {" "}
            Delete
          </button>
        </span>
      </div>
    );
  }
}
export default Post;
