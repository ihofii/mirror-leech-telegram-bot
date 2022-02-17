from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'startx{CMD_INDEX}'
        self.MirrorCommand = f'mirrorx{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzipmirrorx{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipmirrorx{CMD_INDEX}'
        self.CancelMirror = f'cancelx{CMD_INDEX}'
        self.CancelAllCommand = f'cancelallx{CMD_INDEX}'
        self.ListCommand = f'listx{CMD_INDEX}'
        self.SearchCommand = f'searchx{CMD_INDEX}'
        self.StatusCommand = f'statusx{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'usersx{CMD_INDEX}'
        self.AuthorizeCommand = f'authorizex{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorizex{CMD_INDEX}'
        self.AddSudoCommand = f'addsudox{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudox{CMD_INDEX}'
        self.PingCommand = f'pingx{CMD_INDEX}'
        self.RestartCommand = f'restartx{CMD_INDEX}'
        self.StatsCommand = f'statsx{CMD_INDEX}'
        self.HelpCommand = f'helpx{CMD_INDEX}'
        self.LogCommand = f'logx{CMD_INDEX}'
        self.SpeedCommand = f'speedtestx{CMD_INDEX}'
        self.CloneCommand = f'clonex{CMD_INDEX}'
        self.CountCommand = f'countx{CMD_INDEX}'
        self.WatchCommand = f'watchx{CMD_INDEX}'
        self.ZipWatchCommand = f'zipwatchx{CMD_INDEX}'
        self.QbMirrorCommand = f'qbmirrorx{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qbunzipmirrorx{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qbzipmirrorx{CMD_INDEX}'
        self.DeleteCommand = f'delx{CMD_INDEX}'
        self.ShellCommand = f'shellx{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelpx{CMD_INDEX}'
        self.LeechSetCommand = f'leechsetx{CMD_INDEX}'
        self.SetThumbCommand = f'setthumbx{CMD_INDEX}'
        self.LeechCommand = f'leechx{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleechx{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleechx{CMD_INDEX}'
        self.QbLeechCommand = f'qbleechx{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleechx{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleechx{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatchx{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatchx{CMD_INDEX}'
        self.RssListCommand = f'rsslistx{CMD_INDEX}'
        self.RssGetCommand = f'rssgetx{CMD_INDEX}'
        self.RssSubCommand = f'rsssubx{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsubx{CMD_INDEX}'
        self.RssUnSubAllCommand = f'rssunsuballx{CMD_INDEX}'

BotCommands = _BotCommands()
