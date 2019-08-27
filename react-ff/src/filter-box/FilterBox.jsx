import React, { Component, Fragment } from 'react'

export default class FilterBox extends Component {
    constructor (props) {
        super(props)
        this.state = {
            checked: props.checked
        }
    }
    render () {
        const { filter, checked, onToggle } = this.props
        const fbid = 'filter-box-' + filter
        return (
            <Fragment>
                <input type='checkbox' id={fbid} name={fbid} checked={checked} onChange={onToggle}></input>
                <label htmlFor={fbid}>{filter}</label>
            </Fragment>
        )
    }
}