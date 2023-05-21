from argparse import ArgumentParser , RawTextHelpFormatter
from os import get_terminal_size


######################################################################################## 
# #* Credits to @Thijsvanede for making the StructuredFormatter class.
# #? Should I try to shorten this class ? 
class StructuredFormatter(RawTextHelpFormatter):
    """Text formatter for ArgumentParser"""

    def __init__(self, prog, indent_increment=4, width=None):
        """Format text without description on newline"""
        # Bugfix for argparse which does not comput column width properly
        if width is None:
            try:
                width = get_terminal_size(0).columns
            except OSError:
                width = None

        # Call super with infinite max_help_position
        super().__init__(
            prog,
            indent_increment=indent_increment,
            max_help_position=float('inf'),
            width=width
        )

        # Store max default length
        self._default_max_length = 0
        self.   _dest_max_length = 0
        self.   _help_max_length = 0

    def add_argument(self, action):
        """Override: computes maximum length of default"""
        # Call super
        result = super().add_argument(action)
        # Increment _default_max_length
        if action.default and action.nargs != 0:
            self._default_max_length = max(self._default_max_length,
                                           len(str(action.default))) + 1
        if action.dest:
            self._dest_max_length = max(self._dest_max_length,
                len(str(self._format_args(action, action.dest.upper())))) + 1 

        if action.help:
            self._help_max_length = max(self._help_max_length,
                                        len(str(action.help))) + 1 

        # Return result
        return result

    def _format_action(self, action):
        """Add (default=<default>) to action if any"""

        # Format actions regularly
        result = super()._format_action(action)

        # Add default if any
        if action.nargs == '?':
            result = result.split('\n')
            space =  self._help_max_length + self._action_max_length + self._current_indent
            if space + self._default_max_length + 12 <= self._width:
                result[-2] = result[-2] + '{} (optional)'  .format(
                    ' '*max(0, space - len(result[-2]))
                )
            else:
                space = self._width - 12 - self._default_max_length
                result[-1] = result[-1] + '{}(optional)\n'.format(
                    ' '*max(1, space)
                )
            result = '\n'.join(result)

        elif action.default and action.nargs != 0:
            result = result.split('\n')
            space =  self._help_max_length + self._action_max_length + self._current_indent
            if space + self._default_max_length + 12 <= self._width:
                result[-2] = result[-2] + '{} (default = {:>{width}})'  .format(
                    ' '*max(0, space - len(result[-2])),
                    str(action.default),
                    width=self._default_max_length
                )
            else:
                space = self._width - 12 - self._default_max_length
                result[-1] = result[-1] + '{}(default = {:>{width}})\n'.format(
                    ' '*max(1, space),
                    str(action.default),
                    width=self._default_max_length
                )

            result = '\n'.join(result)
        # Return result
        return result

    def _format_action_invocation(self, action):
        """Format actions by showing name only once"""
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar

        else:
            args_string = ""
            parts = []

            # if the Optional doesn't take a value, format is:
            #    -s, --long
            if action.nargs == 0:
                parts.extend(action.option_strings)

            # if the Optional takes a value, format is:
            #    -s ARGS, --long ARGS
            else:
                default = action.dest.upper()
                args_string = " "+self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append(option_string)

            # Join parts
            parts = ', '.join(parts)
            result = "{}{padding}{}".format(parts, args_string, padding=
                ' '*(self._action_max_length-len(parts)-self._dest_max_length-3))

            return result
########################################################################################

parser = ArgumentParser(
    prog="horus",
    description="Fetches the system information.",
    formatter_class=StructuredFormatter ,
    epilog="    If launched with no arguments, \n    The behaviour is the same as with '-c ~/.config/horus/papyri.cfg'."
)


parser.add_argument('-c','--config', help='Path of a config file.',metavar='path')
parser.add_argument('-bg','--background', nargs='+', type = int, help='Background color code.', metavar='R,G,B')
parser.add_argument('-fg','--foreground', nargs='+', type = int, help='Foreground color code.', metavar='R,G,B')

args = parser.parse_args()


