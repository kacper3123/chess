import React from "react";
import { useDrag } from 'react-dnd'
import { ItemTypes } from './Constants'

class Piece extends React.Component {
    render() {
        return (
            <div class={this.props.piece}></div>
            );
}}

export default Piece