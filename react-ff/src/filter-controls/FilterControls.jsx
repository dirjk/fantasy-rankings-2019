import React, { Component } from 'react'

export default class FilterControls extends Component {
    render () {
        const { setAllFilterBoxes } = this.props
        return (
            <div>
                <button onClick={() => {setAllFilterBoxes(false)}}>Clear Filters</button>
                <button onClick={() => {setAllFilterBoxes(true)}}>Show All Filters</button>
            </div>
        )
    }
}