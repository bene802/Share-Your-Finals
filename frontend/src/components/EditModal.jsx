import React, { Component } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

class EditModal extends Component {
  state = {
    post: {
      id: 0,
      user_id: 0,
      author: "",
      title: "",
      date: "",
      content: ""
    }
  };

  componentWillReceiveProps(nextProps) {
    this.setState({
      post: nextProps.edit.edit_post
    });
  }

  titleHandler = event => {
    const post = this.state.post;
    post.title = event.target.value;
    this.setState({ post });
  };
  contentHandler = event => {
    let post = this.state.post;
    post.content = event.target.value;
    this.setState({ post });
  };
  render() {
    return (
      <Modal
        show={this.props.edit.edit_show}
        onHide={() => this.props.handleEditClose()}
      >
        <Modal.Header closeButton>
          <Modal.Title>Edit Post</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>
            <span className="modal-lable">Title:</span>
            <input
              type="text"
              className="form-control"
              defaultValue={this.state.post.title}
              onChange={e => this.titleHandler(e)}
            />
          </p>
          <p>
            <span className="modal-lable">Content:</span>
            <input
              type="text"
              className="form-control"
              defaultValue={this.state.post.content}
              onChange={e => this.contentHandler(e)}
            />
          </p>
        </Modal.Body>
        <Modal.Footer>
          <Button
            variant="secondary"
            onClick={() => this.props.handleEditClose()}
          >
            Close
          </Button>
          <Button
            variant="primary"
            onClick={() => this.props.handleEditSave(this.state.post)}
          >
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
    );
  }
}

export default EditModal;
