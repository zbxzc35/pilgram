# Copyright 2019 Akiomi Kamakura
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PIL import Image

from pilgram import css
from pilgram import util


def maven(im):
    """Applies Maven filter.

    Arguments:
        im: An input image.

    Returns:
        The output image.
    """

    cb = util.or_convert(im, 'RGB')

    cs = util.fill(cb.size, [3, 230, 26])
    cm = css.blending.hue(cb, cs)
    cr = Image.blend(cb, cm, .2)

    cr = css.sepia(cr, .25)
    cr = css.brightness(cr, .95)
    cr = css.contrast(cr, .95)
    cr = css.saturate(cr, 1.5)

    return cr
