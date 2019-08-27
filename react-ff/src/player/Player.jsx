import React, { Component } from 'react'

export default class Player extends Component {
    render () {
        const { player, toggleView } = this.props
        const name = player['player-name']
        const bye = player['bye-week']
        const team = player['team-name']
        const { rank, position } = player
        return (
            <div style={{'paddingLeft': '2px'}}>
                <p><span onClick={toggleView}>[x]</span> {rank} {name} | {position} | {team} | {bye} </p>
            </div>
        )
    }
}