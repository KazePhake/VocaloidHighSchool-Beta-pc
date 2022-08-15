image duongtoitruong="duongtoitruong.jpg"
image chap1="chap1.jpg"
image rindomat="rindomat.png"
image rin="rin.png"
image tronglop="tronglop.jpg"
image lily="Lily.png"
image cantin="cantin.jpg"
image ringiandu="ringiandu.png"
image l="len.png"
image dark="dark.jpg"
image hall="hallway.jpg"
image hanhlang="hanhlang.jpg"
image villain="villain.png"
image kaito="kaito.png"
image miku="miku.png"
image oliver="oliver.png"
image hall2="hall2.jpg"
image rinxlen="rinxlen.png"

define rin = Character("Kagamine Rin", color="#FFFF00")
define lily = Character("Lily", color="#CCFF33")
define l = Character("Kagamine Len", color="FFCC00")
define unknown = Character("unknown")
define damdong = Character("Học Sinh")
define kaito = Character("Kaito", color="#0000CC")
define oliver = Character("Oliver", color="#00FF66")
define miku = Character("Hatsune Miku", color="#00FF66")

label start:
    play music "nhacnen.mp3"
    scene chap1
    "Chap 1"
    scene duongtoitruong
    show rin
    "Bầu trời trong xanh không một gợn mây, gió thổi nhè nhẹ qua hàng cây anh đào bên đường, cánh hoa rơi lả tả tạo thành một cơn mưa hoa tuyệt đẹp"
    rin "(cười mỉm)"
    "Hôm nay là ngày khai gỉang năm học mới"
    "Rin rất vui mừng khi trúng tuyển vào ngôi trường mà cô hằng mơ ước"
    "Trường trung học Vocaloid- ngôi trường nổi tiếng nhất nhì Tokyo, nhưng đó không phải là lí do chính Rin chọn ngôi trường này mà bởi là vì..."
    show rindomat
    with dissolve
    "Rin vô thức đỏ mặt"
    jump vaolop

label vaolop:
    scene tronglop
    show lily
    lily "Xin chào các em, tên cô là Lily"
    lily "Trong thời gian sắp tới, cô sẽ là giáo viên chủ nhiệm của lớp A(lớp chọn, Rin không hiểu vì sao mình lại được vào lớp này)"
    lily "Cô rất hy vọng là chúng ta sẽ hợp tác tốt với nhau"
    lily "Bây giờ các em hãy tự giới thiệu về bản thân mình đi nào"
    "Các học sinh trong lớp lần lượt đứng lên dõng dạc giới thiệu bản thân mình trước mặt mọi người, cuối cùng cũng đến lượt của Rin"
    scene tronglop
    show rin
    rin "Tên mình là Kagamine Rin, sinh nhật là ngày 27 tháng 12"
    rin "Mình rất thích..."
    play sound "mocua.mp3"
    "Rin đang nói thì chợt tiếng mở cửa của ai đó cắt ngang"
    "Một chàng trai có mái tóc vàng óng được buộc gọn thành túm xuất hiện"
    "Cậu ta ngang nhiên ngồi vào chỗ trống nào đó, không để ý đến mọi người xung quanh đang ồ lên kinh ngạc"
    "Tại sao ư?"
    "Cái tên con trai ấy đó có gương mặt giống hệt Rin, giống nhau như hai giọt nước, kể cà màu tóc lẫn màu mắt"
    "Rin sững sờ quan sát tên con trai ấy một cách chăm chú, trong lòng quả thật không tài nào hiểu nổi"
    scene tronglop
    show l
    with dissolve
    l "..."
    l "(ngạc nhiên)"
    scene tronglop
    show lily
    lily "Em có thể tự giới thiệu về mình không?"
    scene tronglop
    show l
    l "Kagamine Len, sinh ngày 27 tháng 12..."
    #play sound "damdongcuoi.mp3"
    "Cả lớp cười ầm lên, không chỉ gương mặt giống nhau, mà còn trùng họ, trùng ngày sinh nữa."
    "Hai người đó là song sinh à?"
    jump cantin
    
label cantin:
    scene dark
    ""
    scene cantin
    play music "nhacnen2.mp3"
    show ringiandu
    rin "KHÔNG!!"
    rin "Tớ và Kagamine-kun không hề quen biết nhau, làm sao là anh em song sinh được?"
    "Vì không nén nổi tò mò, giờ ra chơi mọi người xúm lại bắt Rin và Len để tra khảo"
    unknown "Len, có thật là cậu với Rin chưa gặp nhau bao giờ?"
    scene cantin
    show l
    l "Đúng, tớ và Rin chưa gặp nhau bao giờ..."
    damdong "Gọi bằng tên luôn kìa!"
    unknown "Vậy tại sao cậu và cậu ta lại giống nhau như đúc(quay sang hỏi Rin)"
    "Rin cứng họng, bởi vì cái này thì cô không biết"
    unknown "Len, cậu có biết tại sao không?"
    "Len làm ra vẻ trầm ngâm rồi hỏi lại:"
    l "Rin, cậu sinh ngày mấy tháng mấy?"
    scene cantin
    show rin
    rin "Ừm, 27 tháng 12..."
    scene cantin
    show l
    l "Tôi cũng vậy!"
    damdong "!?"
    "Thế thì sao?"
    l "Cậu không thấy có nhiều giả thiết khoa học đã được đặt ra đã nói rằng: Những người sinh cùng giờ cùng phút cùng giây thì có thể sẽ mang hình hài giống nhau"
    damdong "À ra là vậy"
    "Dường như nhận ra sự mất tự nhiên của Rin, Len liền đứng phắt dậy rồi chạy đi đâu đó, mọi người lập tức đuổi theo và giờ ra chơi kết thúc"
    jump unknown1
    
label unknown1:
    scene hall
    "Bạn sẽ là Rin từ bây giờ"
    "Lựa chọn của bạn sẽ dựa trên những gì mà cô ấy biết hay suy nghĩ"
    "Tầm nhìn của bạn sẽ thu hẹp lại dưới góc nhìn của Rin"
    "Bạn sẽ quyết định tương lai của Kagamine Rin!"
    menu:
        "Đi kiếm và thăm người mình thích":
            jump thamkaito
        "Đi kiếm Len tìm hiểu rõ":
            jump kiemlen1
    
label thamkaito:
    scene hanhlang
    "Rin nhanh chóng chạy đến dãy phòng học của học sinh lớp trên, với mục đích chính là kiếm một người"
    "Là Kaito-senpai"
    "Cô rất nóng lóng muốn cho Kaito-senpai biết rằng mình đã đậu vào chung trường với anh"
    "Nhưng khi cô lên tới dãy phòng lớp trên..."
    jump gapkaito1
    
label kiemlen1:
    "Sau khi hoàn tất bữa ăn của mình xong, cô vẫn còn một thắc mắc lớn trong lòng"
    "Bỏ qua chuyện hôm nay cô đã định làm, cô quyết định đi kiếm Len"
    "Bước ra khỏi lớp, cô đi về hướng mà Len khi nãy bỏ ra khỏi lớp"
    "Tới đầu cầu thang, Rin không biết cậu đã đi lên hay đi xuống"
    menu:
        "Đi xuống":
            jump gaplen1
        "Đi lên":
            jump gapkaito1
        "Hỏi một người nào gần đấy":
            jump hoihocsinh

label hoihocsinh:
    menu:
        "Hỏi một học sinh nữ":
            jump hoinu
        "Hỏi một học sinh nam":
            jump hoinam

label hoinam:
    scene hall
    show rin
    rin "Bạn ơi, cho mình hỏi này chút..."
    scene hall
    show villain
    unknown "Muốn hỏi gì à, em gái dễ thương?"
    rin "(Có chút bực mình) Mình không giỡn với bạn!"
    damdong "(sỗ sàng) Nhưng mình thì muốn!"
    rin "(né ra) Mình chỉ muốn hỏi cậu có thấy Kagamine Len đi đâu không?"
    damdong "(sàm sỡ) Kiếm thằng đó quỡn đó làm gì, đi chơi với anh đi!"
    rin "(sợ hãi) Dừ...Dừng lại!"
    rin "Nếu không t..tôi la lên bây giờ!"
    damdong "Chơi em một lần rồi vô tù cũng được nữa...(Tiến tới)"
    rin "(lùi dần lại)"
    menu:
        "Hét lên":
            jump olivercuu
        "Chạy xuống cầu thang":
            jump gaplen1
        "Chạy lên cầu thang":
            jump gapkaito1
    
label hoinu:
    scene hall
    show rin
    rin "Bạn ơi, cho mình hỏi này chút..."
    damdong "(vui vẻ) Bạn muốn hỏi gì?"
    rin "Nãy giờ bạn cò thấy Kagamine Len đi qua đây không?"
    damdong "À, khi nãy mình có thấy bạn ấy đi qua đây..."
    damdong "(chi tay về phía cầu thang đi lên) Cậu ấy đi lên cầu thang đó!"
    rin "Cám ơn bạn rất nhiều!"
    "Rin chạy lên cầu thang"
    "Cô bỗng bắt gặp một cảnh mà cô không muốn thấy..."
    jump gapkaito1
    
label olivercuu:
    play music "nhacnen3.mp3"
    scene hall
    "Rin hét lên"
    "Cô đã rất sợ hãi"
    "Và thế là..."
    oliver "Này"
    rin "...được cứu rồi..."
    damdong "Tch...Mất vui..."
    "Tên học sinh ấy bỏ đi"
    "Rin thở phào nhẹ nhõm"
    oliver "Bạn có sao không?"
    "Đến lúc này, Rin mới kịp ngẩng lên nhìn xem ai vừa mới cứu mình"
    show oliver
    "Một.. cậu bé?"
    oliver "Nếu cậu đang nghĩ mình là một cậu bé thì quên đi nhé!"
    oliver "Mình 16 tuổi rồi đấy nhé!"
    rin "... vậy nghĩa là...senpai à..."
    rin "Cám...Cám ơn anh!"
    oliver "Không có gì!"
    oliver "Mà em đang định đi đâu thế?"
    rin "Em đang đi kiếm một học sinh tên là Kagamine Len"
    rin "Anh có thấy cậu ấy không?"
    oliver "Hình như anh thấy cậu ấy đi xuống lầu"
    rin "Cám ơn anh!(rồi cô chạy đi)"
    oliver "(quay lại nói lớn) Em tên gì vậy, cô bé dễ thương?"
    rin "Rin..."
    "Tiếo tục chạy, Rin nói to"
    rin "Kagamine Rin, lớp A khối 1, là kouhai của anh đó"
    oliver "(cười mỉm) Lớp A à..."    
    jump gaplen1

label gaplen1:
    scene hall2
    "Rin chạy hộc tốc xuống cầu thang"
    "Cô rất tò mò muốn tìm hiểu thêm về Len, người giống cô y như đúc"
    "Chạy quá nhanh, khi xuống tới cuối cầu thang, cô dừng lại không kịp"
    "Và cô đã tông trúng một người"
    show rinxlen
    l "!!!"
    rin "...thôi chết..."
    "Rin đỏ mặt, Len cũng thế"
    "Cả hai đứng đó một lúc lâu..."
    "Cho đến khi Rin là người chạy đi trước"
    rin "(lí nhí) Xin lỗi cậu!"
    jump endchap1

label gapkaito1:
    scene hanhlang
    "Cô thấy Kaito(người cô thầm thích, và cũng là lí do Rin muốn thi vào trường này) đang đứng nói chuyện vui vẻ với một cô gái"
    "Cô gái đó đang đứng quay lưng lại nên Rin không thể trông thấy gương mặt" 
    "Nhưng chỉ dựa vào mái tóc dài màu xanh lá được buộc gọn sang hai bên trông thật nữ tính và đáng yêu, thân hình thon thả yêu kiều làm Rin có thể lờ mờ đoán ra được, đó là một mỹ nhân tuyệt sắc"
    "Đột nhiên, Rin có cảm giác đau nhói trong tim rằng, liệu Kaito-senpai có thích cô gái đó không nhỉ?"
    "Chỉ mới nghĩ tới khả năng ấy, Rin điếng người không dám suy nghĩ tiếp"
    "Từ đằng xa nhìn thấy mái tóc vàng óng cùng cái nơ trắng như hai cái tai thỏ, Kaito mỉm cười lên tiếng"
    show kaito
    kaito "Rin-chan, vào đi, đừng núp nữa!"
    menu:
        "Vào gặp":
            jump tieptuc1
        "Chạy đi":
            jump gaplen2

label tieptuc1:
    play music "nhacnen1.mp3"
    scene hanhlang
    "Rin giật mình, Kaito-senpai gọi mình, cô chạy nhanh đến đứng bên cạnh anh, khuôn mặt tươi cười như muốn che giấu tâm sự"
    show rin
    rin "Hì, Kaito-senpai, em đã đậu vào trường Vocaloid rồi nè. Anh thấy em mặc đồng phục đẹp không?(thực ra ở đây chả có quy định đồng phục gì ráo :v)"
    "Kaito mỉm cười, nhẹ nhàng xoa đầu cô như anh vẫn thường làm, chỉ bao nhiêu đó thôi cũng đủ làm tim cô đập thình thịch liên hồi"
    scene hanhlang
    show kaito
    kaito "Rin-chan, đây là Hatsune Miku, bạn cùng lớp với anh"
    scene hanhlang
    show miku
    kaito "Miku, đây là Rin-chan mà tớ đã từng kể với cậu"
    "Nhìn từ khoảng cách gần như vậy, Rin mở to mắt kinh ngạc, Miku-senpai không phải là mỹ nhân, mà là đại mỹ nhân"
    "Khuôn mặt hình trái xoan thanh tú, làn da trắng nõn nà, đôi mắt long lanh màu xanh ngọc bích, nụ cười thường trực trên môi, trên người toả ra khí chất thanh tao"
    "Miku-senpai mỉm cười thân thiện"
    miku "Xin chào, Rin-chan!"
    miku "Em quả thật rất giống Len-chan…"
    "Rin nhất thời ngơ ngác, không hiểu ý của Miku-senpai"
    scene hanhlang
    show kaito
    kaito "Rin-chan, chẳng phải lớp em có một nam sinh tên là Kagamine Len sao?"
    "Rin giật mình nhớ ra..."
    kaito "Len là hàng xóm của Miku, anh từng gặp cậu ta, hai đứa đúng là giống nhau đến kỳ lạ!"
    jump endchap1
label gaplen2:
    play music "nhacnen3.mp3"
    scene hall2
    "Rin chạy nhanh xuống dưới lầu"
    "Cô va vào một nguời"
    play sound "mocua.mp3"
    "Cô đúng dậy và xin lỗi"
    oliver "Không sao, mà em có bị gì không?"
    "Rin ngước lên, và trước mặt cô là một...cậu nhóc xem chừng như mới 12,13 tuổi"
    show oliver
    oliver "Em đang nghĩ anh là một cậu nhóc chứ gì?"
    rin "Ơ...ơ"
    oliver "Xin lỗi đi nhá, anh đây 16 tuổi rồi đó"
    rin "..."
    "Cô đã chạy đi rất nhanh, đến nỗi va vào người khác, lại còn là người khối trên"
    rin "(lí nhí) Em xin lỗi ạ"
    oliver "(cười) Không có gì!"
    oliver "Cũng sắp hết tiết rồi, em nên vào lớp nhanh đi!"
    rin "Dạ, xin lỗi đã làm phiền ạ!"
    "Rin chạy đi"
    "Oliver gọi với theo"
    oliver "Em cho anh biết tên được không, cô bé dễ thương?"
    rin "RIN..."
    "Vừa chạy, cô vừa nói lớn"
    rin "Kagamine Rin, lớp A khối 1"
    "Và cô chạy đi mất"
    oliver "(cười mỉm) Lớp A à..."
    jump endchap1
label endchap1:
    play music "nhacgoc.mp3"
    scene dark
    "Hết chap 1"
    "Đây chỉ mới là bản beta, và cốt truyện này mình mượn của một nick tên là minami_1611 trên vnsharing"
    "Mình thấy hay nên mình mới lấy làm visual novel"
    "Mạn phép tác giả cho mình mượn tác phẩm"
    "Tới người chơi: Hiện tại truyện này có tới 20 chap, và vẫn còn nữa, đây chỉ mới chap 1 thôi nhá!"
    return