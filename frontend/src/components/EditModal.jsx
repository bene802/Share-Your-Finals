import React, { Component } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

class EditModal extends Component {
  render() {
    return (
      <Modal show={this.props.show} onHide={() => this.props.handleEditClose()}>
        <Modal.Header closeButton>
          <Modal.Title>Modal heading</Modal.Title>
        </Modal.Header>
        <Modal.Body>Woohoo, you're reading this text in a modal!</Modal.Body>
        <Modal.Footer>
          <Button
            variant="secondary"
            onClick={() => this.props.handleEditClose()}
          >
            Close
          </Button>
          <Button
            variant="primary"
            onClick={() => this.props.handleEditClose()}
          >
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
    );
  }
}

export default EditModal;
