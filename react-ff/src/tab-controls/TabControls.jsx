import React, { Component } from 'react'

export default class TabControls extends Component {
    render () {
        const { changeTab } = this.props
        return (
            <div>
                <button onClick={() => {changeTab('available')}}>Show Available</button>{'  '}
                <button onClick={() => {changeTab('picked')}}>Show Already Picked</button>{'  '}
                <button onClick={() => {changeTab('my team')}}>Show My Team</button>
            </div>
        )
    }
}