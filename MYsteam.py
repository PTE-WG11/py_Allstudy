# -----------------------------------------------------------------------
# PS:
import sys
import urllib

from numpy import unicode


class InStream:
    """
    可以从网络或文件输入
    """

    def __init__(self, fileOrUrl=None):

        self._buffer = ''
        self._stream = None
        self._readingWebPage = False

        if fileOrUrl is None:
            import stdio
            self._stream = sys.stdin  # 从命令行输入
            return

        try:
            if sys.hexversion < 0x03000000:
                self._stream = open(fileOrUrl, 'rU')
            else:
                self._stream = open(fileOrUrl, 'r', encoding='utf-8')
        except IOError:
            try:
                self._stream = urllib.urlopen(fileOrUrl)
                self._readingWebPage = True
            except IOError:
                raise IOError('No such file or URL: ' + fileOrUrl)

    def hasNextLine(self):
        """
        下一行非空，返回True
        """
        if self._buffer != '':
            return True
        else:
            self._buffer = self._stream.readline()
            if sys.hexversion < 0x03000000 or self._readingWebPage:
                self._buffer = self._buffer.decode('utf-8')
            if self._buffer == '':
                return False
            return True

    def readLine(self):
        """
        返回读出的一行
        仅对自动分行（非正常换行）的行会报错
        """
        if not self.hasNextLine():
            raise EOFError()
        s = self._buffer
        self._buffer = ''
        return s.rstrip('\n')

    def __del__(self):
        if self._stream is not None:
            self._stream.close()


class OutStream:
    """
    输出到文件或命令行
    """

    def __init__(self, f=None):  # f是文件名，默认是命令行
        if f is None:
            self._stream = sys.stdout
        else:
            if sys.hexversion < 0x03000000:
                self._stream = open(f, 'w')  # 可以添加错误处理
            else:
                self._stream = open(f, 'w', encoding='utf-8')

    def writeln(self, x=''):
        """
        往流中写入串x，末尾加上换行符
        """
        if sys.hexversion < 0x03000000:
            x = unicode(x)
            x = x.encode('utf-8')
        else:
            x = str(x)
        self._stream.write(x)
        self._stream.write('\n')
        self._stream.flush()

    def __del__(self):
        self._stream.close()
