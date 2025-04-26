import music21
import click

@click.command()
@click.option('--musescore-version', default="4", help='main version of musescore installed')
def main(musescore_version):
    us = music21.environment.UserSettings()
    us['musicxmlPath'] = f'C:\\Program Files\\MuseScore {musescore_version}\\bin\\MuseScore{musescore_version}.exe'
    us['musescoreDirectPNGPath'] = f'C:\\Program Files\\MuseScore {musescore_version}\\bin\\MuseScore{musescore_version}.exe'

if __name__ == '__main__':
    main()