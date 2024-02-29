if await is_active_chat(message.chat.id):
        await put(
            message.chat.id,
            title,
            duration,
            videoid,
            file_path,
            ruser,
            message.from_user.id,
        )
        position = len(fallendb.get(message.chat.id))
        qimg = await gen_qthumb(videoid, message.from_user.id)
        await message.reply_photo(
            photo=qimg,
            caption=f"➻ تمت الاضافة الى قائمة الانتظار{position}\n\n‣ الأسم : [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n‣ الوقت : {duration} ثانية\n‣ بواسطة : {ruser}",
            reply_markup=buttons,
        )
    else:
        stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
        try:
            await pytgcalls.join_group_call(
                message.chat.id,
                stream,
                stream_type=StreamType().pulse_stream,
            )

        except NoActiveGroupCall:
            return await fallen.edit_text(
                "** الكول مش شغال يسطا ."
            )
        except TelegramServerError:
            return await fallen.edit_text(
                "توجد مشكله في سيرفر التليجرام يرجي اعادة تشغيل المحادثه الصوتيه والمحاوله مره اخري ."
            )
        except UnMuteNeeded:
            return await fallen.edit_text(
                f" {BOT_NAME} البوت مكتوم ف الكول,\n\nالرجاء الغاء كتمه {ASS_MENTION} في الكول والمحاوله مره اخري."
            )

        imgt = await gen_thumb(videoid, message.from_user.id)
        await stream_on(message.chat.id)
        await add_active_chat(message.chat.id)
        await message.reply_photo(
            photo=imgt,
            caption=f"➻ تم التشغيل بنجاح\n\n‣ الأسم : [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n‣ الوقت : {duration} ثانية\n‣ بواسطة : {ruser}",
            reply_markup=buttons,
        )

    return await fallen.delete()
