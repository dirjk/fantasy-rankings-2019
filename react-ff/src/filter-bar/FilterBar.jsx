import React, { Component } from 'react'

export default class FilterBar extends Component {
    constructor (props) {
        super(props)
        this.state = {
            searchTerm: ''
        }
        this.handleChange = this.handleChange.bind(this)
    }
    handleChange (event) {
        const newSearchTerm = event.target.value
        this.props.handleSearchChange(newSearchTerm)
        this.setState({ searchTerm: newSearchTerm })
    }
    render () {
        const { searchTerm } = this.state
        return (
            <div>
                <span style={{ padding: '4px'}}>Filter Players:</span>
                <input type='text' value={searchTerm} onChange={this.handleChange}/>
            </div>
        )
    }
}